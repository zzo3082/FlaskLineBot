# Flask Line Bot

使用 flask 寫 linebot 來熟悉 python 專案

# 套件管理

本專案使用以下方式管理套件與依賴：

1. **使用** `requirements.txt`\
   使用 `pip` 安裝 `requirements.txt` 中列出的套件：

   ```bash
   pip install -r requirements.txt
   ```

2. **使用** `pyproject.toml`\
   如果專案使用 `pyproject.toml` 定義依賴，可以使用以下指令安裝：

   ```bash
   uv pip install .
   ```

   或使用 `uv` 同步依賴：

   ```bash
   uv sync
   ```

3. **使用** `uv`\
   使用 `uv` 創建虛擬環境並安裝依賴：

   ```bash
   uv venv
   uv pip install -r requirements.txt
   ```

   或直接根據 `uv.lock` 同步依賴：

   ```bash
   uv sync
   ```

4. **使用虛擬環境的好處**

   - **隔離性**：虛擬環境為每個專案提供獨立的 Python 環境，避免依賴衝突。
   - **可重現性**：通過 `requirements.txt` 或 `uv.lock`，其他開發者可輕鬆重現相同的環境。
   - **乾淨性**：防止全局安裝套件影響其他專案或系統環境。
   - **靈活性**：允許在同一台機器上使用不同版本的 Python 和套件。

## License

This project is licensed under the MIT License - see the LICENSE file for details.