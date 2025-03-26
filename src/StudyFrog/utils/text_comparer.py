import spacy
import threading

from typing import *

from concurrent.futures import ProcessPoolExecutor


__all__: Final[List[str]] = ["TextComparer"]


class TextComparer:
    """
    A class for comparing the similarity between two texts using spaCy models.

    This class provides a convenient interface for comparing the similarity between two texts using
    either a fast or deep spaCy model. The class uses a singleton pattern to ensure that only one
    instance of the class is created per process.

    Attributes:
        fast_model_name (str): The name of the fast spaCy model to use.
        deep_model_name (str): The name of the deep spaCy model to use.
        preprocess (bool): Indicates whether to preprocess the text before comparing.
        fast_nlp (Optional[spacy.Language]): The loaded fast spaCy model.
        deep_nlp (Optional[spacy.Language]): The loaded deep spaCy model.
        logger (Logger): A logger for logging messages.
    """

    _shared_instance: Optional[Type["TextComparer"]] = None
    _lock: threading.Lock = threading.Lock()

    @classmethod
    def instance(
        cls,
        fast_model: str = "en_core_web_md",
        deep_model: str = "en_core_web_trf",
        preprocess: bool = True,
    ) -> Type["TextComparer"]:
        """
        Returns the shared instance of the TextComparer class.

        Args:
            fast_model (str, optional): The name of the fast spaCy model to use. Defaults to 'en_core_web_md'.
            deep_model (str, optional): The name of the deep spaCy model to use. Defaults to 'en_core_web_trf'.
            preprocess (bool, optional): Indicates whether to preprocess the text before comparing. Defaults to True.

        Returns:
            Type[TextComparer]: The shared instance of the TextComparer class.
        """
        with cls._lock:
            if cls._shared_instance is None:
                cls._shared_instance = super(TextComparer, cls).__new__(cls)
                cls._shared_instance.init(
                    deep_model=deep_model,
                    fast_model=fast_model,
                    preprocess=preprocess,
                )
        return cls._shared_instance

    def init(
        self,
        deep_model: str = "en_core_web_trf",
        fast_model: str = "en_core_web_md",
        preprocess: bool = True,
    ) -> None:
        """
        Initializes the TextComparer instance.

        Args:
            deep_model (str, optional): The name of the deep spaCy model to use. Defaults to 'en_core_web_trf'.
            fast_model (str, optional): The name of the fast spaCy model to use. Defaults to 'en_core_web_md'.
            preprocess (bool, optional): Indicates whether to preprocess the text before comparing. Defaults to True.

        Returns:
            None
        """
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)
        self.fast_model_name = fast_model
        self.deep_model_name = deep_model
        self.preprocess = preprocess
        self.fast_nlp: Optional[spacy.Language] = None
        self.deep_nlp: Optional[spacy.Language] = None

    def _load_model(
        self,
        deep: bool = False,
    ) -> spacy.Language:
        """
        Loads the appropriate spaCy model based on the given 'deep' flag.

        Args:
            deep (bool, optional): Indicates whether to use the deep model. Defaults to False.

        Returns:
            spacy.Language: The loaded spaCy model.
        """
        try:
            if deep:
                # Load the deep model if not already loaded
                if self.deep_nlp is None:
                    self.deep_nlp = spacy.load(
                        self.deep_model_name, disable=["ner", "parser"]
                    )
                return self.deep_nlp
            else:
                # Load the fast model if not already loaded
                if self.fast_nlp is None:
                    self.fast_nlp = spacy.load(
                        self.fast_model_name, disable=["ner", "parser"]
                    )
                return self.fast_nlp
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to load '{self.__class__.__name__}' model: {e}"
            )

            # Return the original text
            return text

    def _preprocess_text(
        self,
        text: str,
        deep: bool = False,
    ) -> str:
        """
        Preprocesses the given text using the appropriate spaCy model.

        Args:
            text (str): The text to be preprocessed.
            deep (bool, optional): Indicates whether to use the deep model. Defaults to False.

        Returns:
            str: The preprocessed text.
        """
        try:
            # Load the appropriate model
            nlp: spacy.Language = self._load_model(deep=deep)

            # Load the text into a spacy document
            doc: spacy.Doc = nlp(text.lower())

            # Remove stop words and keep only the lemmatized words
            return (
                " ".join([token.lemma_ for token in doc if not token.is_stop])
                if self.preprocess
                else text
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run '_preprocess_text' method from '{self.__class__.__name__}': {e}"
            )

            # Return the original text
            return text

    def _confidence_level(
        self,
        score: float,
    ) -> Tuple[str, str]:
        """
        Determines the confidence level based on the similarity score.

        Confidence levels are based on the similarity score and are as follows:
        - High: 0.95 <= score < 1.0 (nearly identical with minimal differences)
        - Medium: 0.75 <= score < 0.95 (similar but with noticeable differences)
        - Low: 0.50 <= score < 0.75 (share some meaning but differ significantly)
        - Very Low: score < 0.50 (largely dissimilar or unrelated)

        Args:
            score (float): The similarity score between the texts.

        Returns:
            Tuple[str, str]: A tuple containing the confidence level and a description of the confidence level.
        """
        if score >= 0.95:
            return "High", "The texts are nearly identical with minimal differences."
        elif score >= 0.75:
            return "Medium", "The texts are similar but have noticeable differences."
        elif score >= 0.50:
            return "Low", "The texts share some meaning but differ significantly."
        else:
            return "Very Low", "The texts are largely dissimilar or unrelated."

    def compare(
        self,
        original: str,
        copy: str,
        deep_analysis: bool = False,
        auto_switch: bool = True,
    ) -> Dict[str, float | str]:
        """
        Compares the similarity between the original and copy texts.

        Args:
            original (str): The original text.
            copy (str): The copy text.
            deep_analysis (bool, optional): Indicates whether to use the deep model. Defaults to False.
            auto_switch (bool, optional): Indicates whether to automatically switch to the deep model if the similarity score is below 0.75. Defaults to True.

        Returns:
            Dict[str, float | str]: A dictionary containing the similarity score, confidence level, explanation of the confidence level, and the model used.
        """
        try:
            # Preprocess the original text using the appropriate model
            original_cleaned: str = self._preprocess_text(original, deep=deep_analysis)

            # Preprocess the copy text using the appropriate model
            copy_cleaned: str = self._preprocess_text(copy, deep=deep_analysis)

            # Load the appropriate model
            nlp: spacy.Language = self._load_model(deep_analysis)

            # Create spacy documents from the preprocessed texts
            doc1, doc2 = nlp(original_cleaned), nlp(copy_cleaned)

            # Calculate the similarity score between the documents
            score: float = doc1.similarity(doc2)

            # If the similarity score is below 0.75 and auto_switch is True, re-run the comparison with the deep model
            if auto_switch and not deep_analysis and score < 0.75:
                return self.compare(
                    original, copy, deep_analysis=True, auto_switch=False
                )

            # Calculate the confidence level based on the similarity score
            (
                confidence,
                explanation,
            ) = self._confidence_level(score)

            # Return a dictionary containing the similarity score, confidence level, explanation of the confidence level, and the model used
            return {
                "similarity_score": round(score, 4),
                "confidence": confidence,
                "explanation": explanation,
                "model_used": (
                    self.deep_model_name if deep_analysis else self.fast_model_name
                ),
            }
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'compare' method from '{self.__class__.__name__}': {e}"
            )

            # Return a dictionary indicating an exception has occurred
            return {
                "similarity_score": None,
                "confidence": None,
                "explanation": None,
                "model_used": None,
            }

    def _parallel_compare(
        self,
        text_pair: Tuple[str, str],
        deep_analysis: bool = False,
        auto_switch: bool = True,
    ) -> Dict[str, float | str]:
        """
        Compares a pair of texts using the specified analysis model.

        This function uses the specified model to compare the similarity
        between two texts and determines the confidence level of the comparison.

        Args:
            text_pair (Tuple[str, str]): A tuple containing the original and copy texts.
            deep_analysis (bool, optional): Indicates whether to use the deep model. Defaults to False.
            auto_switch (bool, optional): Indicates whether to automatically switch to the deep model if the similarity score is below 0.75. Defaults to True.

        Returns:
            Dict[str, float | str]: A dictionary containing the similarity score, confidence level, explanation of the confidence level, and the model used.
        """
        try:
            # Compare the text pair using the specified analysis settings
            return self.compare(
                auto_switch=auto_switch,
                copy=text_pair[1],
                deep_analysis=deep_analysis,
                original=text_pair[0],
            )
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'parallel_compare' method from '{self.__class__.__name__}': {e}"
            )

            # Return a dictionary indicating an exception has occurred
            return {
                "similarity_score": None,
                "confidence": None,
                "explanation": None,
                "model_used": None,
            }

    def batch_compare(
        self,
        text_pairs: List[Tuple[str, str]],
        deep_analysis: bool = False,
        auto_switch: bool = True,
        max_workers: int = 4,
    ) -> List[Dict[str, float | str]]:
        """
        Compares a list of text pairs in parallel using the specified analysis model.

        This function is a wrapper around the `compare` method that allows you to compare
        multiple text pairs in parallel. It uses the `concurrent.futures` module to create
        a pool of worker processes and map the `compare` method to each pair in the list.

        Args:
            text_pairs: A list of tuples containing the original and copy texts to compare.
            deep_analysis: Indicates whether to use the deep model. Defaults to False.
            auto_switch: Indicates whether to automatically switch to the deep model if the similarity score is below 0.75. Defaults to True.
            max_workers: The maximum number of worker processes to create. Defaults to 4.

        Returns:
            A list of dictionaries containing the similarity score, confidence level, explanation of the confidence level, and the model used for each comparison.
        """
        try:
            with ProcessPoolExecutor(max_workers=max_workers) as executor:
                results: List[Dict[str, float | str]] = list(
                    executor.map(
                        lambda pair: self._parallel_compare(
                            pair, deep_analysis, auto_switch
                        ),
                        text_pairs,
                    )
                )

            return results
        except Exception as e:
            # Log an error message indicating an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'batch_compare' method from '{self.__class__.__name__}': {e}"
            )

            # Return an empty list indicating an exception has occurred
            return []
