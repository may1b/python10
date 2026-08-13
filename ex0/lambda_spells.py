from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    powers = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(powers),
        'min_power': min(powers),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Ice Wand', 'power': 78, 'type': 'weapon'},
        {'name': 'Earth Shield', 'power': 60, 'type': 'armor'},
    ]
    mages = [
        {'name': 'Alex', 'power': 75, 'element': 'fire'},
        {'name': 'Jordan', 'power': 92, 'element': 'lightning'},
        {'name': 'Riley', 'power': 58, 'element': 'water'},
        {'name': 'Sage', 'power': 88, 'element': 'earth'},
    ]
    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    print("Testing power filter...")
    strong = power_filter(mages, 80)
    print(f"Mages with power >= 80: "
          f"{', '.join(map(lambda mage: mage['name'], strong))}")

    print("Testing spell transformer...")
    print(' '.join(spell_transformer(spells)))

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
          f"Avg: {stats['avg_power']}")


if __name__ == "__main__":
    main()
