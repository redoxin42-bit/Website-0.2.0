from sqlalchemy import create_all, Column, Integer, String, Boolean
# В среде S-01 используем SQLite для экономии памяти на Render
# Храним: ID пользователя, название купленного промпта и статус выдачи.
