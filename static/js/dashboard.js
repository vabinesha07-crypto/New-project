document.addEventListener(
    "DOMContentLoaded",
    function () {

        const cards =
            document.querySelectorAll(
                ".service-card"
            );


        cards.forEach(
            function (card) {

                card.addEventListener(
                    "keydown",
                    function (event) {

                        if (
                            event.key === "Enter"
                            ||
                            event.key === " "
                        ) {

                            event.preventDefault();

                            card.click();
                        }

                    }
                );

            }
        );

    }
);