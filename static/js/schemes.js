document.addEventListener(
    "DOMContentLoaded",
    function () {

        const searchInput =
            document.querySelector(
                'input[name="q"]'
            );


        if (!searchInput) {
            return;
        }


        searchInput.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key === "Enter"
                ) {

                    const form =
                        searchInput.closest(
                            "form"
                        );


                    if (form) {

                        form.submit();

                    }

                }

            }
        );

    }
);