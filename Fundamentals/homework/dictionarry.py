inventory = {
    'gold':500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
inventory['backpack'].remove('dagger')
print(inventory)
inventory['gold'] += 50
print(inventory)
