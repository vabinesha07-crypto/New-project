document.addEventListener(
    "DOMContentLoaded",
    function () {

        const form =
            document.getElementById(
                "profileForm"
            );

        if (!form) {
            return;
        }

        const phone =
            document.getElementById(
                "phone"
            );

        const aadhaar =
            document.getElementById(
                "aadhaar"
            );

        if (phone) {

            phone.addEventListener(
                "input",
                function () {

                    phone.value =
                        phone.value
                            .replace(
                                /\D/g,
                                ""
                            )
                            .slice(
                                0,
                                10
                            );

                }
            );

        }

        if (aadhaar) {

            aadhaar.addEventListener(
                "input",
                function () {

                    aadhaar.value =
                        aadhaar.value
                            .replace(
                                /\D/g,
                                ""
                            )
                            .slice(
                                0,
                                12
                            );

                }
            );

        }

        form.addEventListener(
            "submit",
            function (event) {

                const phoneValue =
                    phone
                        ? phone.value.trim()
                        : "";

                const aadhaarValue =
                    aadhaar
                        ? aadhaar.value.trim()
                        : "";

                if (
                    phoneValue &&
                    phoneValue.length !== 10
                ) {

                    event.preventDefault();

                    alert(
                        "Mobile number must contain 10 digits."
                    );

                    return;
                }

                if (
                    aadhaarValue &&
                    aadhaarValue.length !== 12
                ) {

                    event.preventDefault();

                    alert(
                        "Aadhaar number must contain 12 digits."
                    );

                }

            }
        );

    }
);