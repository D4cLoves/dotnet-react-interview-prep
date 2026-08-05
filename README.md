# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 17 — 2026-08-05)

### 🏷️ Тема: `React`
### ❓ Зачем нужен хук `useEffect` и как работает его массив зависимостей?

#### 💡 Ответ и разбор:
Хук `useEffect` используется для выполнения **побочных эффектов (side-effects)** в функциональных компонентах: запрос данных с сервера, подписки на события, манипуляции с DOM.

**Массив зависимостей (Dependency Array):**

1. `useEffect(() => { ... })` — без массива. Вызывается **после каждого рендера** компонента.
2. `useEffect(() => { ... }, [])` — пустой массив. Вызывается **только один раз** при монтировании компонента (Mount).
3. `useEffect(() => { ... }, [count, user])` — вызывается при первом рендере, а также при изменении значений `count` или `user`.

**Cleanup функция (Очистка):**
Если эффект возвращает функцию, она вызывается перед размонтированием компонента или перед следующим запуском эффекта.

```tsx
useEffect(() => {
  const timer = setInterval(() => console.log('tick'), 1000);
  return () => clearInterval(timer); // Очистка таймера
}, []);
```

---

## 📚 Архив пройденных вопросов

| День | Тема | Вопрос |
|---|---|---|
| День 001 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-001.md) |
| День 002 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-002.md) |
| День 003 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-003.md) |
| День 004 | `React / TypeScript` | [Что такое Virtual DOM в React и как работает алгоритм Reconciliation (Diffing)?](questions/day-004.md) |
| День 005 | `ASP.NET Core` | [Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?](questions/day-005.md) |
| День 006 | `C#` | [Как работают `async` и `await` под капотом в C#?](questions/day-006.md) |
| День 007 | `React` | [В чем разница между `useMemo` и `useCallback`?](questions/day-007.md) |
| День 008 | `ASP.NET Core / Security` | [Как устроена JWT (JSON Web Token) аутентификация?](questions/day-008.md) |
| День 009 | `EF Core` | [Что такое проблема N+1 запросов в EF Core и как её избежать?](questions/day-009.md) |
| День 010 | `React / State` | [В чем разница между Redux Toolkit, TanStack Query (React Query) и Zustand?](questions/day-010.md) |
| День 011 | `C#` | [Что такое Value Types (типы значений) и Reference Types (ссылочные типы)? ГДЕ они хранятся?](questions/day-011.md) |
| День 012 | `ASP.NET Core` | [Что такое SignalR и когда его следует использовать?](questions/day-012.md) |
| День 013 | `React` | [Что такое React StrictMode и почему компоненты рендерятся дважды в разработке?](questions/day-013.md) |
| День 014 | `ASP.NET Core / Architecture` | [Что такое паттерн CQRS и библиотека MediatR?](questions/day-014.md) |
| День 015 | `TypeScript` | [В чем разница между `type` и `interface` в TypeScript?](questions/day-015.md) |
| День 016 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-016.md) |
| День 017 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-017.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
