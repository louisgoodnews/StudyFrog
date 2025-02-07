"""
Author: lodego
Date: 2025-02-05
"""

from core.flashcard import (
    ImmutableFlashcard,
    MutableFlashcard,
    FlashcardManager,
    FlashcardModel,
    FlashcardConverter,
    FlashcardFactory,
)

from utils.logger import Logger


def debug_flashcard() -> None:
    logger: Logger = Logger.get_logger(name="debug")

    logger.debug("\n🔹 DEBUGGING FLASHCARD MODULE 🔹\n")

    try:
        # Test: FlashcardManager initialisieren
        manager = FlashcardManager()
        logger.debug("✅ FlashcardManager erfolgreich erstellt.")

        # Test: Flashcard erstellen
        test_flashcard = ImmutableFlashcard(
            front_text="Was ist die Hauptstadt von Frankreich?", back_text="Paris"
        )

        created_flashcard = manager.create(test_flashcard)
        if created_flashcard:
            logger.debug(f"✅ Flashcard erstellt: {created_flashcard.to_dict()}")
        else:
            logger.error("❌ Fehler beim Erstellen der Flashcard.")

        # Test: Flashcard abrufen per ID
        fetched_flashcard = manager.get_by_id(created_flashcard.id)
        if fetched_flashcard:
            logger.debug(f"✅ Flashcard per ID gefunden: {fetched_flashcard.to_dict()}")
        else:
            logger.error("❌ Fehler beim Abrufen der Flashcard per ID.")

        # Test: Flashcard abrufen per UUID
        fetched_flashcard_uuid = manager.get_by_uuid(created_flashcard.uuid)
        if fetched_flashcard_uuid:
            logger.debug(
                f"✅ Flashcard per UUID gefunden: {fetched_flashcard_uuid.to_dict()}"
            )
        else:
            logger.error("❌ Fehler beim Abrufen der Flashcard per UUID.")

        # Test: Flashcard löschen
        delete_success = manager.delete(created_flashcard)
        if delete_success:
            logger.debug("✅ Flashcard erfolgreich gelöscht.")
        else:
            logger.error("❌ Fehler beim Löschen der Flashcard.")

        # Test: Flashcard-Zählung
        count = manager.count()
        logger.info(f"📊 Aktuelle Anzahl an Flashcards: {count}")

    except Exception as e:
        logger.critical(f"❌ Fehler im Debug-Script: {e}")


if __name__ == "__main__":
    debug_flashcard()
