import functools
import time
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power", args[-1] if args else 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("Testing power validator...")

    @power_validator(min_power=20)
    def mighty_spell(power: int) -> str:
        return f"Mighty spell cast with {power} power"

    print(mighty_spell(25))
    print(mighty_spell(10))

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise ValueError("The spell fizzled")

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def waaaaaaagh() -> str:
        return "Waaaaaaagh spelled !"

    print(waaaaaaagh())

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf the Grey"))
    print(MageGuild.validate_mage_name("Gandalf123"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
