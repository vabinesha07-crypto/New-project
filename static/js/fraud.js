document.addEventListener(
    "DOMContentLoaded",
    function () {

        const form =
            document.getElementById(
                "fraudForm"
            );


        const result =
            document.getElementById(
                "fraudResult"
            );


        const riskLevel =
            document.getElementById(
                "riskLevel"
            );


        const reasons =
            document.getElementById(
                "riskReasons"
            );


        const recommendation =
            document.getElementById(
                "recommendation"
            );


        if (!form) {
            return;
        }


        form.addEventListener(
            "submit",
            async function (event) {

                event.preventDefault();


                const message =
                    document.getElementById(
                        "message"
                    ).value.trim();


                if (!message) {

                    alert(
                        "Please enter a message."
                    );

                    return;
                }


                result.hidden = false;


                riskLevel.textContent =
                    "Checking message...";


                reasons.innerHTML =
                    "";


                recommendation.textContent =
                    "";


                try {

                    const response =
                        await fetch(
                            "/api/fraud/check",
                            {
                                method: "POST",

                                headers: {
                                    "Content-Type":
                                        "application/json"
                                },

                                body: JSON.stringify({
                                    message: message
                                })
                            }
                        );


                    const data =
                        await response.json();


                    if (!response.ok) {

                        throw new Error(
                            data.message
                            ||
                            "Unable to check message."
                        );

                    }


                    riskLevel.textContent =
                        data.risk_level
                        ||
                        "Risk assessment";


                    recommendation.textContent =
                        data.recommendation
                        ||
                        "";


                    if (
                        Array.isArray(
                            data.reasons
                        )
                    ) {

                        if (
                            data.reasons.length === 0
                        ) {

                            const item =
                                document.createElement(
                                    "li"
                                );


                            item.textContent =
                                "No common warning signs detected.";


                            reasons.appendChild(
                                item
                            );

                        } else {

                            data.reasons.forEach(
                                function (reason) {

                                    const item =
                                        document.createElement(
                                            "li"
                                        );


                                    item.textContent =
                                        reason;


                                    reasons.appendChild(
                                        item
                                    );

                                }
                            );

                        }

                    }


                } catch (error) {

                    riskLevel.textContent =
                        "Unable to complete check";


                    recommendation.textContent =
                        error.message;

                }

            }
        );

    }
);