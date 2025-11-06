from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication
from encode_thread import EncodeThread
from decode_thread import DecodeThread

class MainController:
    def __init__(self, ui):
        self.ui = ui
        self.thread = None

        self.ui.Button_input.clicked.connect(self.select_input_folder)
        self.ui.Button_output.clicked.connect(self.select_output_folder)
        self.ui.Button_Run.clicked.connect(self.run_function)
        self.ui.Button_Cancel.clicked.connect(self.close_app)

        # CHANGED: theo dõi khi người dùng chọn chức năng để bật/tắt ô SIZE FILE
        self.ui.Funtion_choice.currentIndexChanged.connect(self.toggle_size_input)

    # CHANGED: thêm hàm kiểm soát bật/tắt ô dung lượng
    def toggle_size_input(self):
        action = self.ui.Funtion_choice.currentText()
        if action == "Biên Dịch":
            self.ui.size_limit_input.setEnabled(False)
        else:
            self.ui.size_limit_input.setEnabled(True)

    def select_input_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Chọn thư mục INPUT")
        if folder:
            self.ui.Input_text.setText(folder)

    def select_output_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Chọn thư mục OUTPUT")
        if folder:
            self.ui.output_text.setText(folder)

    def run_function(self):
        input_folder = self.ui.Input_text.text().strip()
        output_folder = self.ui.output_text.text().strip()
        action = self.ui.Funtion_choice.currentText()
        size_text = self.ui.size_limit_input.text().strip()  # lấy giá trị nhập vào

        if not input_folder or not output_folder:
            QMessageBox.warning(None, "Thiếu thông tin", "📂 Vui lòng chọn đủ INPUT và OUTPUT")
            return

        try:
            max_size_mb = float(size_text) if size_text else 35.0
        except ValueError:
            QMessageBox.warning(None, "Lỗi", "Vui lòng nhập dung lượng hợp lệ (số).")
            return

        self.ui.label_status.setText(f"🔄 {action}...")

        if action == "Mã Hóa":
            self.thread = EncodeThread(input_folder, output_folder, max_size_mb)
            self.thread.finished.connect(self.done)
        else:
            self.thread = DecodeThread(input_folder, output_folder)
            self.thread.finished_msg.connect(self.done)

        self.thread.start()

    def done(self, msg):
        self.ui.label_status.setText(msg)
        QMessageBox.information(None, "Trạng thái", msg)

    def close_app(self):
        QApplication.quit()
