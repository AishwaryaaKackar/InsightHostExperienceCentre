import re


# =====================================================
# Restricted Terms
# =====================================================

restricted_keywords=[

    "salary",
    "employee salary",
    "payroll",
    "compensation",
    "employee pay",

    "confidential",
    "internal data",
    "private data",

    "employee data",
    "employee details",

    "password",
    "secret",
    "token",
    "credential",

    "phone number",
    "mobile number",

    "personal email",
    "email address",

    "bank account",
    "account number",

    "hr records",
    "financial records"

]


# =====================================================
# Validate Input
# =====================================================

def validate_input(text):

    if not text:

        return{

            "allowed":False,

            "message":
            "Please provide a valid question."
        }


    text=text.strip()


    if len(text)==0:

        return{

            "allowed":False,

            "message":
            "Please provide a valid question."
        }


    if len(text)>500:

        return{

            "allowed":False,

            "message":
            "Question too long."
        }


    text_lower=text.lower()


    for word in restricted_keywords:

        if word in text_lower:

            return{

                "allowed":False,

                "message":

                (
                    "Sorry, I can help with publicly "
                    "available company information, "
                    "but I cannot provide private or "
                    "confidential employee information."
                )
            }


    text_clean=re.sub(

        r"[^\w\s]",

        "",

        text

    )


    return{

        "allowed":True,

        "text":text_clean
    }