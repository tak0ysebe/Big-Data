import pandas as pd

class Table:
    def __init__(self, url) -> None:
        self.table = pd.read_csv(url, sep=",") #считывание таблицы
        self.columns = self.table.columns
        pass
    
    def print_table(self):
        print(self.table)
        
    def split(self, num):
        self.table_1 = self.table.iloc[:num]
        self.table_2 = self.table.iloc[num:]
        return ("table_1 and table_2 created")
    
    def concat(table1, table2, axis=1):
        print(table2.table)
        return pd.concat([table1.table, table2.table], axis=axis)
    
    def get_rows_by_number(self, start, stop=None, copy_table=False):   
        if copy_table:
            if stop:
                self.df = self.table.iloc[start:stop+1] #строки
            else:
                self.df = self.table.iloc[start]
            return self.df           
        else:
            if stop:
                self.table = self.table.iloc[start:stop+1] #сохранение в файл
            else:
                self.table = self.table.iloc[start]
            return self.table

    def get_rows_by_index(self, *args, copy_table=False):
        try:
            self.df = pd.DataFrame(columns=self.table.columns).apply(pd.to_numeric)
            column = self.columns[0]
            gener = [arg for arg in args]
            if copy_table:
                self.df = self.df.append(self.table.loc[self.table[f"{column}"].isin(gener)])
                self.df.index = range(0, len(self.df))
                return self.df
            else:
                self.df = self.df.append(self.table.loc[self.table[f"{column}"].isin(gener)])
                self.df.index = range(0, len(self.df))
                self.table = self.df
                return self.table
        except:
            return 'перебор аргументов'
        
    def get_column_types(self, by_number=True):
        try:
            if by_number:
                return self.table.dtypes
            else:
                return self.table.dtypes
        except:
            return 'перебор аргументов'

     
    def set_column_types(self, types_dict, by_number=True):
        try:
            if by_number == False:
                self.table = self.table.astype(types_dict)
                return self.table
            else: 
                columns = self.table.columns
                for key in types_dict:
                    self.table = self.table.astype({columns[key-1]: types_dict[key]})
                return self.table
        except:
            return 'НЕКОРРЕКТНЫЙ ввод параметра by_number'    

    def get_values(self, column=0):
        try:
            self.col_arr = self.table.iloc[:,column].tolist()
            return [int(x) for x in self.col_arr]
        except IndexError:
            return 'ошибка ввода аргумента'
        except:
            return 'много аргументов'

    def get_value(self, column=0):
        try:
            self.data = self.table.iloc[0][column]
            return self.data
        except IndexError:
            return 'ошибка ввода аргумента'
    
    def set_values(self, values, column=0):
        self.change_col = self.table.iloc[0:4]
        try:
            self.change_col[self.columns[column]] = values
            return self.change_col
        except ValueError:
            return 'Неверное количество значений'
        except TypeError:
            return 'много аргументов'

    def set_value(self, stolb, value, column=0):
        try:
            self.change_num = self.table.iloc[stolb]
            self.change_num[column] = value
            return self.change_num
        except IndexError:
            return 'перебор аргументов'
        
    
trol1 = Table("D:/Загрузки/Финашка/nuclear_weapons.csv")
trol2 = Table("D:/Загрузки/Финашка/nuclear_weapons.cont.csv")
#print(trol1.table)
#print(trol1.get_rows_by_number(4, 7, True))
#print(trol1.get_rows_by_index(1, 5, 48, 100, 213, copy_table=False))
#print(trol1.get_column_types())
#print(trol1.set_column_types({4: "int64"}, True))
#print(trol1.get_values(3))
#print(trol1.get_value(2))
#print(trol1.set_values(1,7))
#print(trol1.set_value(5, 4))
#trol1.print_table()
#print(pd.set_option('display.max_rows', None))#для вывода таблицы
#print(trol1.split(10))#со следующей строкой
#print(trol1.table_1)
print(Table.concat(trol1, trol2,0))

