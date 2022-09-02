
class Logger:
    MAX_LENGTH = 50

    @classmethod
    def Title(cls, message):
        length = (cls.MAX_LENGTH - len(message)) // 2
        equal = "=" * length
        print(f"\n{equal}[ {message} ]{equal}")

    @classmethod
    def SubTitle(cls, message, align='center'):
        length = (cls.MAX_LENGTH - len(message)) // 2
        emptyHalf = " " * length
        emptyFull = " " * (cls.MAX_LENGTH - len(message) - 1)
        star = "*" * (cls.MAX_LENGTH + 3)

        match align:
            case 'left': print(f"\n( {message} ){emptyFull}")
            case 'center': print(f"\n{emptyHalf}( {message} ){emptyHalf}")
            case 'right': print(f"\n{emptyFull}( {message} )")
        print(star)

    @classmethod
    def Section(cls, title, number=0.0):
        print(f"\n\t[ {title} ]")
        print(f"|{number}|")
        print(f"\t{'-' * (cls.MAX_LENGTH - 1)}")

    @classmethod
    def Space(cls):
        print(f"\n\t{'- ' * (cls.MAX_LENGTH // 2)}")

    @classmethod
    def Divider(cls):
        print(f"\n{'-' * (cls.MAX_LENGTH + 3)}")

    @classmethod
    def PrintTab(cls, message, level=1):
        match level:
            case 0:
                print(message)
            case 1:
                print(f"\t{message}")
            case 2:
                print(f"\t\t{message}")

    @classmethod
    def PrintList(cls, items, level=1):
        messages = list(items)
        print()
        for message in messages:
            match level:
                case 0:
                    print(f"-> {message}")
                case 1:
                    print(f"\t-> {message}")
                case 2:
                    print(f"\t\t-> {message}")
        print()

