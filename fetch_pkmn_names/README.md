# Fetch Pokemon Names

This is a simple(ish) Python script to pull a list of Pokémon names from [PokeAPI](https://pokeapi.co/).

I needed a list of strings to populate a Trie data structure, for autocompletion. So, I'm fetching Pokémon names.

Funnily, this info is available pretty much anywhere, but weirdly tricky to get in raw-list form without parsing or sanitizing its source in some way (by parsing/scraping HTML or similar).

This script aims to fetch names without timing-out the host server, and to keep track of its place if it does timeout.