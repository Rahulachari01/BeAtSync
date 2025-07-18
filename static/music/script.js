// syncapp/static/syncapp/js/script.js

document.addEventListener("DOMContentLoaded", function () {
  // Select all play/pause buttons
  const playPauseButtons = document.querySelectorAll(".play-pause-btn");

  // Add click listener to each button
  playPauseButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Get the ID of the audio element controlled by this button
      const audioId = this.dataset.audioId;
      const currentAudio = document.getElementById(audioId);

      if (!currentAudio) {
        console.error(`Audio element with ID ${audioId} not found.`);
        return;
      }

      // Pause all other audio elements first
      document.querySelectorAll("audio").forEach((audio) => {
        if (audio !== currentAudio && !audio.paused) {
          audio.pause();
          // Update the text of the button associated with this paused audio
          const otherButton = document.querySelector(
            `button[data-audio-id="${audio.id}"]`
          );
          if (otherButton) {
            otherButton.textContent = "Play";
          }
        }
      });

      // Now, toggle the play/pause state of the current audio
      if (currentAudio.paused) {
        currentAudio.play();
        this.textContent = "Pause"; // Change button text to 'Pause'
      } else {
        currentAudio.pause();
        this.textContent = "Play"; // Change button text to 'Play'
      }
    });

    // Optional: Add an event listener to reset button text when audio ends
    const audioIdForButton = button.dataset.audioId;
    const audioElementForButton = document.getElementById(audioIdForButton);
    if (audioElementForButton) {
      audioElementForButton.addEventListener("ended", function () {
        button.textContent = "Play";
      });
    }
  });

  console.log("Audio player script loaded."); // For debugging
});
const playButton = document.getElementById("play-button");
const audioPlayer = document.getElementById("coolie-song");

playButton.addEventListener("click", () => {
  audioPlayer.play();
});
