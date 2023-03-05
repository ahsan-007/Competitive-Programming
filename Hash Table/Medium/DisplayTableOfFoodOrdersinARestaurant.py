# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_orders = {}
        dishes = {}
        for order in orders:
            if order[1] not in table_orders:
                table_orders[order[1]] = {}

            if order[2] not in table_orders[order[1]]:
                table_orders[order[1]][order[2]] = 0

            table_orders[order[1]][order[2]] += 1

            if order[2] not in dishes:
                dishes[order[2]] = True
                
        dishes = list(dishes.keys())
        dishes.sort()

        tables = list(table_orders.keys())
        tables = [int(table) for table in tables]
        tables.sort()
        
        formatted_tables = [['Table'] + dishes]
        for table in tables:
            table = str(table)
            table_row = [table]
            for dish in dishes:
                if dish in table_orders[table]:
                    table_row.append(str(table_orders[table][dish]))
                else:
                    table_row.append('0')
            formatted_tables.append(table_row)
        return formatted_tables


print(Solution().displayTable([["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], [
      "David", "3", "Fried Chicken"], ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]))

print(Solution().displayTable([["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], [
      "Amadeus", "12", "Fried Chicken"], ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]))
