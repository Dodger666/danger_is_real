from model.archbrick_engine import Hex

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
            pass
            # // Sorting the open list to get the tile with the lowest F.
            self.open_path_tile = sorted(self.open_path_tile, key=lambda hex: (hex.f(), -hex.g))
            current_hex = self.open_path_tile[0]
            #
            # // Removing the current tile from the open list and adding it to the closed list.
            # openPathTiles.Remove(currentTile);
            # closedPathTiles.Add(currentTile);
            #
            # int g = currentTile.g + 1;
            #
            # // If there is a target tile in the closed list, we have found a path.
            # if (closedPathTiles.Contains(endPoint))
            # {
            #     break;
            # }
            #
            # // Investigating each adjacent tile of the current tile.
            # foreach (Tile adjacentTile in currentTile.adjacentTiles)
            # {
            #     // Ignore not walkable adjacent tiles.
            #     if (adjacentTile.isObstacle)
            #     {
            #         continue;
            #     }
            #
            #     // Ignore the tile if it's already in the closed list.
            #     if (closedPathTiles.Contains(adjacentTile))
            #     {
            #         continue;
            #     }
            #
            #     // If it's not in the open list - add it and compute G and H.
            #     if (!(openPathTiles.Contains(adjacentTile)))
            #     {
            #         adjacentTile.g = g;
            #         adjacentTile.h = GetEstimatedPathCost(adjacentTile.position, endPoint.position);
            #         openPathTiles.Add(adjacentTile);
            #     }
            #     // Otherwise check if using current G we can get a lower value of F, if so update it's value.
            #     else if (adjacentTile.F > g + adjacentTile.h)
            #     {
            #         adjacentTile.g = g;
            #     }
            # }


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

