#!/usr/bin/env python3


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(k, int(v))
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k in inventory:
            inventory[k] += 1
        else:
            inventory.setdefault(k, 1)
    return inventory


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    stuff = addToInventory(stuff, dragonLoot)
    displayInventory(stuff)


if __name__ == '__main__':
    main()
