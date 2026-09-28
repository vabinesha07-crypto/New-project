from urllib.parse import urlparse


OFFICIAL_DOMAINS = {

    "scholarships.gov.in",

    "pmsvanidhi.mohua.gov.in",

    "pmkisan.gov.in"

}


def is_official_link(
    url
):

    try:

        hostname = (
            urlparse(url)
            .hostname
            or ""
        ).lower()


        return (
            hostname in OFFICIAL_DOMAINS
            or hostname.endswith(
                ".gov.in"
            )
            or hostname.endswith(
                ".nic.in"
            )
        )


    except Exception:

        return False