from model.archbrick_model import Hex


class AStarPathfinding:

    def __init__(self):

        self.open_path_tile = []
        self.closed_path_tiles = []

    def find_path(self, hex_start: Hex, hex_end: Hex):

        # Prepare the start tile.
        current_hex: Hex = hex_start

        current_hex.g = 0
        current_hex.h = self._get_estimated_path_cost(hex_start, hex_end)

        # Add the start tile to the open list.
        self.open_path_tile.append(current_hex)

        while len(self.open_path_tile) != 0:
            # // Sorting the open list to get the tile with the lowest F.
            self.open_path_tile = sorted(self.open_path_tile, key=lambda hex: (hex.f(), -hex.g))
            current_hex = self.open_path_tile[0]

            # Removing the current tile from the open list and adding it to the closed list.
            self.open_path_tile = [hex for hex in self.open_path_tile if current_hex.q != hex.q
                                   and current_hex.r != hex.r and current_hex.s != hex.s]
            self.closed_path_tiles.append(current_hex)

            g = current_hex.g + 1

            if self._is_hex_contained(self.closed_path_tiles, hex_end):
                break

            # Investigating each adjacent tile of the current tile.
            # foreach (Tile adjacentTile in currentTile.adjacentTiles)
            for adj_hex in current_hex.adj_hexes:
                # Ignore not walkable adjacent tiles.
                if adj_hex.terrain_height > current_hex.terrain_height:
                    continue

                # Ignore the tile if it's already in the closed list.
                if self._is_hex_contained(self.closed_path_tiles, adj_hex):
                    continue

                # If it's not in the open list - add it and compute G and H.
                if not self._is_hex_contained(self.open_path_tile, adj_hex):
                    adj_hex.g = g
                    adj_hex.h = self._get_estimated_path_cost(adj_hex, hex_end)
                    self.open_path_tile.append(adj_hex)
                    # Otherwise check if using current G we can get a lower value of F, if so update it's value.
                elif adj_hex.f() > g + adj_hex.h:
                    adj_hex.g = g

        final_path_hexes = []

        # Backtracking - setting the final path.
        if hex_end in self.closed_path_tiles:

            current_hex = hex_end
            final_path_hexes.append(current_hex)
            for g_val in range(hex_end.g-1, -1,-1):

                # current_hex = self.closed_path_tiles.Find(x => x.g == i && currentTile.adjacentTiles.Contains(x))
                current_hex = next((hex for hex in self.closed_path_tiles if hex.g == g_val and
                                    self._is_hex_contained(current_hex.adj_hexes, hex)))
                final_path_hexes.append(current_hex)

            final_path_hexes.reverse()

        return final_path_hexes

    # Returns estimated path cost from given start position to target position of hex tile using Manhattan distance.
    def _get_estimated_path_cost(self, starting_hex: Hex, target_hex: Hex):
        return max(abs(starting_hex.q-target_hex.q), abs(starting_hex.r-target_hex.r), abs(starting_hex.s-target_hex.s))

    def _is_hex_contained(self, hex_col: [Hex], a_hex: Hex):
        for hex in hex_col:
            if hex.q == a_hex.q and hex.r == a_hex.r and hex.s == a_hex.s:
                return True
        return False

