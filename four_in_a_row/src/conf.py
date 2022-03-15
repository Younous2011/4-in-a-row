from dataclasses import dataclass

@dataclass
class Conf:
    nb_rows:int = 5
    nb_columns:int = 8
    side:int = 120
    n_rows_in_a_row:int = 4
    n_set:int = 3