import sqlite3

class ProductModel:
    def __init__(self):
        # Tên file database
        self.db_name = "minh_tri_store.db"
        # Tạo kết nối duy trì xuyên suốt để các hàm sau dùng được self.cursor
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """Tạo bảng nếu chưa tồn tại"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            price REAL, 
            size TEXT, 
            stock INTEGER, 
            category TEXT, 
            image_path TEXT)''')
        self.conn.commit()

    def get_all_products(self):
        """Lấy tất cả sản phẩm"""
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def add_product(self, data):
        """Thêm sản phẩm mới (data là một tuple)"""
        query = "INSERT INTO products (name, price, size, stock, category, image_path) VALUES (?,?,?,?,?,?)"
        self.cursor.execute(query, data)
        self.conn.commit()

    def update_product(self, p_id, name, price, stock, category, image_path):
        """Cập nhật sản phẩm theo ID"""
        query = "UPDATE products SET name=?, price=?, stock=?, category=?, image_path=? WHERE id=?"
        self.cursor.execute(query, (name, price, stock, category, image_path, p_id))
        self.conn.commit()

    def delete_product(self, p_id):
        """Xóa sản phẩm theo ID"""
        self.cursor.execute("DELETE FROM products WHERE id=?", (p_id,))
        self.conn.commit()

    def __del__(self):
        """Đóng kết nối khi đối tượng bị hủy"""
        if hasattr(self, 'conn'):
            self.conn.close()