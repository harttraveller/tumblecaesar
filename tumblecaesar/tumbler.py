import random
import string


class Tumbler:
    def __init__(
        self,
        seed: int,
        layers: int,
        chars: list[str] = list(string.ascii_letters + string.digits),
    ) -> None:
        self.__chars = chars
        self.__chars_count = len(self.__chars)
        self.__indices = list(range(self.__chars_count))
        self.__ord = dict(zip(self.__chars, self.__indices))
        self.__seed = seed
        self.__layers = layers

    def enc(self, message: str) -> str:
        message, message_length = [self.__ord[i] for i in message], len(message)
        ordinal_sum = sum([(i + 1) * v for i, v in enumerate(message)])
        for _ in range(self.__layers):
            message = [
                random.Random((i + self.__seed) * ordinal_sum).sample(
                    self.__indices, self.__chars_count
                )[message[i]]
                for i in range(message_length)
            ]
        return "".join([self.__chars[i] for i in message]) + f"-{str(ordinal_sum)}"

    def dec(self, message: str) -> str:
        message = message.split("-")
        message, ordinal_sum = message[0], int(message[1])
        message, message_length = [self.__ord[i] for i in message], len(message)
        for _ in range(self.__layers):
            message = [
                random.Random((i + self.__seed) * ordinal_sum)
                .sample(self.__indices, self.__chars_count)
                .index(message[i])
                for i in range(message_length)
            ]
        return "".join([self.__chars[i] for i in message])
