"""
Author: lodego
Date: 2025-04-03
"""

import numpy
import threading

from datetime import datetime, timedelta
from sentence_transformers import SentenceTransformer, util
from typing import *

from utils.constants import Constants
from utils.dispatcher import Dispatcher
from utils.events import Events
from utils.logger import Logger
from utils.miscellaneous import Miscellaneous


__all__: Final[List[str]] = ["TextAnalyzer"]


class TextAnalyzer:
    """
    A singleton class responsible for analyzing text data.

    The class provides a single shared instance of the TextAnalyzer class,
    accessible using the `instance` class method.

    The class provides methods to load and access the SentenceTransformer model,
    and to compute the similarity between two pieces of text.
    """

    _shared_instance: Optional[Type["TextAnalyzer"]] = None
    _lock: Final[threading.Lock] = threading.Lock()

    @classmethod
    def __new__(
        cls,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ) -> Type["TextAnalyzer"]:
        """
        Creates a new instance of the TextAnalyzer class.

        If the instance does not exist, creates a new one by calling the parent class
        constructor and initializes it by calling the `init` method of the class.

        If the instance already exists, returns the existing instance.

        Args:
            model_name (str): The name of the model to be loaded.
            Defaults to "sentence-transformers/all-MiniLM-L6-v2".

        Returns:
            TextAnalyzer: The created or existing instance of TextAnalyzer class.
        """
        if cls._shared_instance is None:
            with cls._lock:
                if cls._shared_instance is None:
                    cls._shared_instance = super(TextAnalyzer, cls).__new__(cls)
                    cls._shared_instance.init(model_name=model_name)
        return cls._shared_instance

    def init(
        self,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ) -> None:
        """
        Initializes the TextAnalyzer instance.

        This method sets up the logger for the class and initializes
        the model-related attributes.

        Args:
            model_name (str): The name of the model to be loaded.

            Defaults to "sentence-transformers/all-MiniLM-L6-v2".

        Returns:
            None
        """

        # Set up the logger for this instance
        self.logger: Final[Logger] = Logger.get_logger(name=self.__class__.__name__)

        # Initialize the dispatcher
        self.dispatcher: Final[Dispatcher] = Dispatcher()

        # Initialize the time limit attribute
        self.time_limit: int = 600

        # Initialize the timestamp attribute
        self.timestamp: datetime = Miscellaneous.get_current_datetime()

        # Initialize the model attribute as None
        self._model: Optional[SentenceTransformer] = None

        # Initialize the model name as an empty string
        self._model_name: str = model_name

    @property
    def model(self) -> Optional[SentenceTransformer]:
        """
        Returns the SentenceTransformer model currently loaded.

        Returns:
            Optional[SentenceTransformer]: The SentenceTransformer model currently loaded.
        """
        return self._model

    @model.setter
    def model(
        self,
        value: SentenceTransformer,
    ) -> None:
        """
        Sets the SentenceTransformer model to be loaded.

        Args:
            value (SentenceTransformer): The SentenceTransformer model to be loaded.
        """
        self._model = value

    @property
    def model_name(self) -> str:
        """
        Returns the name of the model currently loaded.

        Returns:
            str: The name of the model currently loaded.
        """
        return self._model_name

    @model_name.setter
    def model_name(
        self,
        value: str,
    ) -> None:
        """
        Sets the name of the model to be loaded.

        Args:
            value (str): The name of the model to be loaded.
        """
        self._model_name = value

    def _encode(
        self,
        sentences: Union[str, List[str]],
    ) -> Union[numpy.ndarray, List[numpy.ndarray]]:
        """
        Encodes the given sentences into numerical embeddings using the SentenceTransformer model.

        This method loads the SentenceTransformer model using the model name
        and then uses it to encode the given sentences into a list of numerical
        embeddings.

        Args:
            sentences (Union[str, List[str]]): The sentences to be encoded.

        Returns:
            Union[numpy.ndarray, List[numpy.ndarray]]: The numerical embeddings of the given sentences.

        Raises:
            Exception: If an exception occurs while attempting to run the 'encode' method.
        """
        try:
            # Load the SentenceTransformer model if not already loaded
            self._load_model()

            if not isinstance(
                sentences,
                list,
            ):
                # Convert the senetenes to a list if is not already a list
                sentences = [sentences]

            # Encode the sentences using the loaded model
            return self.model.encode(
                sentences=sentences,
                convert_to_numpy=True,
            )
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'encode' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def _get_similarity(
        self,
        original: Union[List[str], str],
        compare_to: Union[List[str], str],
        on_completion_callback: Optional[Callable[[float], None]] = None,
    ) -> Optional[float]:
        """
        Calculates the cosine similarity between the given sentences and returns the result.

        This method encodes the given sentences into numerical embeddings
        using the SentenceTransformer model and then calculates the cosine
        similarity between the two embeddings.

        Args:
            compare_to (Union[List[str], str]): The second sentence to be compared.
            on_completion_callback (Optional[Callable[[float], None]]): A callback to be called when the similarity calculation is complete.
            original (Union[List[str], str]): The first sentence to be compared.

        Returns:
            Optional[float]: The cosine similarity between the given sentences if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run the 'get_similarity' method.
        """
        try:
            # Dispatch the TEXT_ANALYZER_ANALYSIS_STARTEDin the GLOBAL_NAMESPACE
            self.dispatcher.dispatch(
                event=Events.TEXT_ANALYZER_ANALYSIS_STARTED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Encode the original sentence
            original_embedding: List[str] = self._encode(sentences=original)

            # Encode the compare_to sentence
            compare_to_embedding: List[str] = self._encode(sentences=compare_to)

            # Unload or schedule to unload the model
            self._unload_model()

            # Dispatch the TEXT_ANALYZER_ANALYSIS_COMPLETED the GLOBAL_NAMESPACE
            self.dispatcher.dispatch(
                event=Events.TEXT_ANALYZER_ANALYSIS_COMPLETED,
                namespace=Constants.GLOBAL_NAMESPACE,
            )

            # Calculate the cosine similarity between the two embeddings
            result: float = float(
                util.cos_sim(
                    a=original_embedding,
                    b=compare_to_embedding,
                )
            )

            # Call the on completion callback if provided
            if on_completion_callback:
                on_completion_callback(result)

            # Return the result
            return result
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_similarity' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def _load_model(self) -> None:
        """
        Loads the SentenceTransformer model if it is not already loaded.

        This method attempts to create an instance of the SentenceTransformer
        using the model name. If an exception occurs during model loading, it logs
        the error and re-raises the exception.

        Raises:
            Exception: If an exception occurs while attempting to load the model.
        """
        try:
            # Check if the model is not already loaded
            if self.model is None:
                # Load the model using the specified model name
                self.model = SentenceTransformer(self.model_name)

                # Update the timestamp to the current time
                self.timestamp = Miscellaneous.get_current_datetime()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'load_model' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def _unload_model(self) -> None:
        """
        Unloads the SentenceTransformer model if the time since the last load
        exceeds the time limit.

        This method checks if the difference between the current timestamp and
        the timestamp when the model was last loaded exceeds the time limit.
        If so, it sets the model to None, updates the timestamp, and logs the
        unloading event.

        Raises:
            Exception: If an exception occurs while unloading the model.
        """
        try:
            # Calculate the time difference between the current time and the last loaded time
            time_difference = Miscellaneous.get_current_datetime() - self.timestamp

            # Check if the time difference exceeds the time limit
            if time_difference > timedelta(seconds=self.time_limit):
                # Unload the model by setting it to None
                self.model = None

                # Update the timestamp to the current time
                self.timestamp = Miscellaneous.get_current_datetime()

                # Log an info message indicating the model was unloaded
                self.logger.info(message=f"Model unloaded due to exceeding time limit.")

            # Schedule the next execution of the unload method
            threading.Timer(
                function=self._unload_model,
                interval=float(self.time_limit),
            ).start()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'unload_model' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e

    def get_similarity(
        self,
        original: Union[List[str], str],
        compare_to: Union[List[str], str],
        on_completion_callback: Optional[Callable[[float], None]] = None,
    ) -> Optional[float]:
        """
        Computes the cosine similarity between two sentences asynchronously.

        Args:
            original (Union[List[str], str]): The first sentence to be compared.
            compare_to (Union[List[str], str]): The second sentence to be compared.
            on_completion_callback (Optional[Callable[[float], None]]): A callback to be called when the similarity calculation is complete.

        Returns:
            Optional[float]: The cosine similarity between the given sentences if no exception occurs. Otherwise, None.

        Raises:
            Exception: If an exception occurs while attempting to run the 'get_similarity' method.
        """
        try:
            # Start a new thread to compute similarity asynchronously
            return threading.Thread(
                target=self._get_similarity,
                args=(
                    original,
                    compare_to,
                    on_completion_callback,
                ),
                daemon=True,
            ).start()
        except Exception as e:
            # Log an error message indicating that an exception has occurred
            self.logger.error(
                message=f"Caught an exception while attempting to run 'get_similarity' method from '{self.__class__.__name__}': {e}"
            )

            # Re-raise the exception to the caller
            raise e
