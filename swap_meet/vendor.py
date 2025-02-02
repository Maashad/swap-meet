""" Initiation of class Vendor """

class Vendor:
		""" Represents a unique entity from which one can trade items. """
		def __init__(self, inventory=None):
				""" Initiate class vendor with empty inventory. """
				self.inventory = [] if inventory is None else inventory

		def add (self, item):
			""" Adds an item to inventory and returns the added item """
			self.inventory.append(item)
			return item


		def remove (self, item):
				""" Remove one matching item from the 'inventory' and returns it. Returns False if no matching item. """
				for i, k in enumerate(self.inventory):
					if k == item:
						self.inventory.pop(i)
						return item
				return False

		def get_by_id(self, id):
				""" Get item with matching id from inventory, return None if not found """
				for item in self.inventory:
						if item.id == id:
								return item
				return None

		def swap_items(self, other_vendor, my_item, their_item):
			""" Removes items from both vendor's inventories and swaps them. If item from one vendor is not present, no items will be swapped. """
			#Remove items from both inventories
			other_remove = other_vendor.remove(their_item)
			if not other_remove:
				return False
			self_remove = self.remove(my_item)
			if not self_remove:
				other_vendor.add(their_item)
				return False
			#Add items to both inventories
			self.add(their_item)
			other_vendor.add(my_item)
			return True

		def swap_first_item(self, other_vendor):
			""" Swaps the first item in each vendor's inventory. """
			if not (self.inventory and other_vendor.inventory):
				return False

			self_first = self.inventory[0]

			self.inventory[0] = other_vendor.inventory[0]
			other_vendor.inventory[0] = self_first

			return True
		
		def get_by_category(self, category):
			"""Return items in vendor's inventory matching category"""
			return [item for item in self.inventory if item.get_category() == category]
		
		def get_best_by_category(self, category):
			"""Return best item in given category from inventory"""
			items = self.get_by_category(category)
			if not items:
				return None
			best_item = max(items, key=lambda item: item.condition)
			return best_item

		def swap_best_by_category(self, other_vendor, my_priority, their_priority):
			"""Swap best item in other's preferred category between two vendors"""
			other_item = other_vendor.get_best_by_category(my_priority)
			my_item = self.get_best_by_category(their_priority)

			if not (my_item and other_item):
				return False
			
			self.swap_items(other_vendor, my_item, other_item)

			return True

		def swap_by_newest(self, other_vendor):
			"""Swap newest item in own inventory with newest item in other vendor's inventory"""
			if not (self.inventory and other_vendor.inventory):
				return False
			
			other_item = min(other_vendor.inventory, key=lambda item: item.age)
			my_item = min(self.inventory, key=lambda item: item.age)
			
			self.swap_items(other_vendor, my_item, other_item)

			return True

