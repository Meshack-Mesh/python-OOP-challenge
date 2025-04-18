from pet import Pet

# Create a pet named Max
my_pet = Pet("Lola")
print(f"🐶 Creating pet: {my_pet.name}")

# Perform some actions
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("roll over")
my_pet.train("play dead")

# Show current status
my_pet.get_status()
