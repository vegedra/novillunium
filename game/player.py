class Player:
    def __init__(self):
        self.room = "Sala Inicial"
        self.inventory = []
        self.revealed_items = {}  # Armazena itens que já foram revelados por sala

    def move(self, direction, rooms):
        dir_map = {"norte":"north", "north":"north", "sul":"south", "south":"south",
                   "leste":"east", "east":"east", "oeste":"west", "west":"west"}
        dir_key = dir_map.get(direction.lower())
        if dir_key and dir_key in rooms[self.room]:
            self.room = rooms[self.room][dir_key]
            return f"Você se move para {self.room}."
        return "Não é possível ir nessa direção."

    def look(self, rooms):
        """Olhar ou procurar na sala. Revela itens se houver."""
        room = rooms[self.room]
        desc = room["desc"]
        # Se a sala tiver item e ainda não foi revelado, avisa que há algo
        if "item" in room:
            if self.room not in self.revealed_items:
                self.revealed_items[self.room] = True
                desc += " Você sente que há algo aqui..."
            else:
                desc += f" Você vê aqui: {room['item']}."
        return desc

    def pick_item(self, rooms):
        """Pega o item só se já foi revelado"""
        room = rooms[self.room]
        if "item" in room:
            if self.room in self.revealed_items:
                item_name = room["item"]
                self.inventory.append(item_name)
                del room["item"]
                del self.revealed_items[self.room]  # Remove da revelação
                return f"Você pegou {item_name}."
            else:
                return "Você não sabe o que pegar. Talvez precise procurar primeiro."
        return "Não há nenhum item aqui."
