
'''openapi2markdown swagger.yml  swagger.md'''


import streamlit as st
import subprocess
import tempfile
import os

st.title("📄 OpenAPI → Markdown")
f = st.file_uploader("Выберите .yml", type=["yml", "yaml"])

if f:
    try:
        with tempfile.TemporaryDirectory() as tmp:
            in_path = os.path.join(tmp, "in.yml")
            out_path = os.path.join(tmp, "out.md")

            with open(in_path, "wb") as fp:
                fp.write(f.getvalue())

            # Запускаем ТУ САМУЮ команду, что работает в терминале
            result = subprocess.run([
                "openapi2markdown", in_path, out_path
            ], capture_output=True, text=True, encoding="utf-8")

            if result.returncode != 0:
                st.error(f"❌ Ошибка:\n{result.stderr}")
            else:
                with open(out_path, "r", encoding="utf-8") as fp:
                    st.download_button("⬇️ Скачать api.md", fp.read(), "api.md")
                st.success("✅ Готово!")
    except Exception as e:
        st.error(f"💥 {e}")


