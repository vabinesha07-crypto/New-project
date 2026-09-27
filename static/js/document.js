document.addEventListener(
    "DOMContentLoaded",
    function () {

        const form =
            document.getElementById(
                "documentForm"
            );


        const resultBox =
            document.getElementById(
                "documentResult"
            );


        const resultStatus =
            document.getElementById(
                "resultStatus"
            );


        const resultSummary =
            document.getElementById(
                "resultSummary"
            );


        const resultChecks =
            document.getElementById(
                "resultChecks"
            );


        if (!form) {
            return;
        }


        form.addEventListener(
            "submit",
            async function (event) {

                event.preventDefault();


                const fileInput =
                    document.getElementById(
                        "document"
                    );


                const typeInput =
                    document.getElementById(
                        "document_type"
                    );


                if (
                    !fileInput.files.length
                ) {

                    alert(
                        "Please choose a document."
                    );

                    return;
                }


                if (!typeInput.value) {

                    alert(
                        "Please select a document type."
                    );

                    return;
                }


                const formData =
                    new FormData();


                formData.append(
                    "document",
                    fileInput.files[0]
                );


                formData.append(
                    "document_type",
                    typeInput.value
                );


                resultBox.hidden = false;


                resultStatus.textContent =
                    "Checking document...";


                resultSummary.textContent =
                    "Please wait while the document is analyzed.";


                resultChecks.innerHTML =
                    "";


                try {

                    const response =
                        await fetch(
                            "/api/document/check",
                            {
                                method: "POST",
                                body: formData
                            }
                        );


                    const data =
                        await response.json();


                    if (!response.ok) {

                        throw new Error(
                            data.message
                            ||
                            "Unable to check document."
                        );

                    }


                    resultStatus.textContent =
                        data.status
                        ||
                        "Check completed";


                    resultSummary.textContent =
                        data.summary
                        ||
                        "";


                    if (
                        Array.isArray(
                            data.checks
                        )
                    ) {

                        data.checks.forEach(
                            function (check) {

                                const row =
                                    document.createElement(
                                        "div"
                                    );


                                row.className =
                                    "check-row";


                                const label =
                                    document.createElement(
                                        "span"
                                    );


                                label.textContent =
                                    check.label
                                    ||
                                    "Check";


                                const status =
                                    document.createElement(
                                        "strong"
                                    );


                                status.textContent =
                                    check.ok
                                    ? " ✓ Passed"
                                    : " ✕ Needs attention";


                                status.className =
                                    check.ok
                                    ? "check-ok"
                                    : "check-fail";


                                row.appendChild(
                                    label
                                );


                                row.appendChild(
                                    status
                                );


                                resultChecks.appendChild(
                                    row
                                );

                            }
                        );

                    }

                } catch (error) {

                    resultStatus.textContent =
                        "Unable to complete check";


                    resultSummary.textContent =
                        error.message;


                }

            }
        );

    }
);