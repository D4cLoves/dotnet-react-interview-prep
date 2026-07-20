# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 1 — 2026-07-21)

### 🏷️ Тема: `ASP.NET Core`
### ❓ В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?

#### 💡 Ответ и разбор:
В встроенном DI контейнере ASP.NET Core есть три основных времени жизни (Lifetime):

1. **Transient (`AddTransient`)**:
   * Экземпляр создается **каждый раз**, когда запрашивается из контейнера.
   * Используется для легких сервисов без состояния (stateless).

2. **Scoped (`AddScoped`)**:
   * Экземпляр создается **один раз на каждый HTTP-запрос** (в рамках одного Scope).
   * Подходит для сервисов, хранящих состояние в рамках запроса, например, `DbContext` в EF Core.

3. **Singleton (`AddSingleton`)**:
   * Экземпляр создается **один раз** при первом обращении и живет всё время работы приложения.
   * Используется для кэшей, синглтон-конфигураций или сервисов с тяжелой инициализацией.

```csharp
builder.Services.AddTransient<IMyTransientService, MyTransientService>();
builder.Services.AddScoped<IMyScopedService, MyScopedService>();
builder.Services.AddSingleton<IMySingletonService, MySingletonService>();
```

---

## 📚 Архив пройденных вопросов

| День | Тема | Вопрос |
|---|---|---|
| День 001 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-001.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
