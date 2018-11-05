class Gender():
    MALE = "m"
    FEMALE = "f"
    NONE = "-"
    CHOICES = (
        (MALE,"Male"),
        (FEMALE,"Female"),
        (NONE,"None")
    )

class IdType():
    DNI = "DNI"
    LC = "LC"
    OTHER = 'oth'
    CHOICES = (
        (DNI,"D.N.I."),
        (LC,"L.C."),
        (OTHER,"Other")
    )
