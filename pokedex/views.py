from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Gengar", "Eevee"]
    return render(request, 'index.html', {"pokemons": pokemons})

def pokemon_details(request, pokemon):
    return render(request, 'details.html', {"pokemon": pokemon})

