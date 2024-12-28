document.querySelectorAll(".card").forEach((card) => {
    card.addEventListener("click", () => {
        const cardTitle = card.querySelector("h3") || card.querySelector("p");
        if (cardTitle) {
            alert("You clicked on " + cardTitle.textContent.trim());
        } else {
            console.error("No suitable element found inside the card.");
        }
    });
});
