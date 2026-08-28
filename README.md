# 🚀 Daily C# / ASP.NET & React Q&A

Добро пожаловать в ежедневную базу знаний по **C#, ASP.NET Core и React**! 
Каждый день здесь автоматически публикуется новый разбор реального вопроса с собеседований.

---

## 📌 Вопрос Дня (День 40 — 2026-08-28)

### 🏷️ Тема: `React / State`
### ❓ В чем разница между Redux Toolkit, TanStack Query (React Query) и Zustand?

#### 💡 Ответ и разбор:
Они решают разные задачи менеджмента состояния:

1. **TanStack Query (React Query)**:
   * Специализирован для **Server State** (асинхронные данные с API).
   * Автоматически кэширует, обновляет в фоновом режиме (stale-while-revalidate), обрабатывает загрузку и ошибки.

2. **Redux Toolkit**:
   * Глобальное **Client State** с единственным хранилищем (Single Source of Truth).
   * Подходит для огромных корпоративных приложений со сложной логикой клиента.

3. **Zustand**:
   * Минималистичный и быстрый менеджер глобального состояния без лишнего шаблонного кода (boilerplate).
   * Идеален как легкая альтернатива Redux.

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
| День 018 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-018.md) |
| День 019 | `React / TypeScript` | [Что такое Virtual DOM в React и как работает алгоритм Reconciliation (Diffing)?](questions/day-019.md) |
| День 020 | `ASP.NET Core` | [Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?](questions/day-020.md) |
| День 021 | `C#` | [Как работают `async` и `await` под капотом в C#?](questions/day-021.md) |
| День 022 | `React` | [В чем разница между `useMemo` и `useCallback`?](questions/day-022.md) |
| День 023 | `ASP.NET Core / Security` | [Как устроена JWT (JSON Web Token) аутентификация?](questions/day-023.md) |
| День 024 | `EF Core` | [Что такое проблема N+1 запросов в EF Core и как её избежать?](questions/day-024.md) |
| День 025 | `React / State` | [В чем разница между Redux Toolkit, TanStack Query (React Query) и Zustand?](questions/day-025.md) |
| День 026 | `C#` | [Что такое Value Types (типы значений) и Reference Types (ссылочные типы)? ГДЕ они хранятся?](questions/day-026.md) |
| День 027 | `ASP.NET Core` | [Что такое SignalR и когда его следует использовать?](questions/day-027.md) |
| День 028 | `React` | [Что такое React StrictMode и почему компоненты рендерятся дважды в разработке?](questions/day-028.md) |
| День 029 | `ASP.NET Core / Architecture` | [Что такое паттерн CQRS и библиотека MediatR?](questions/day-029.md) |
| День 030 | `TypeScript` | [В чем разница между `type` и `interface` в TypeScript?](questions/day-030.md) |
| День 031 | `ASP.NET Core` | [В чем разница между Transient, Scoped и Singleton временно́й жизнью сервисов в Dependency Injection?](questions/day-031.md) |
| День 032 | `React` | [Зачем нужен хук `useEffect` и как работает его массив зависимостей?](questions/day-032.md) |
| День 033 | `C# / EF Core` | [В чем ключевая разница между `IEnumerable<T>` и `IQueryable<T>`?](questions/day-033.md) |
| День 034 | `React / TypeScript` | [Что такое Virtual DOM в React и как работает алгоритм Reconciliation (Diffing)?](questions/day-034.md) |
| День 035 | `ASP.NET Core` | [Что такое Middleware в ASP.NET Core и как работает конвейер обработки запроса (Pipeline)?](questions/day-035.md) |
| День 036 | `C#` | [Как работают `async` и `await` под капотом в C#?](questions/day-036.md) |
| День 037 | `React` | [В чем разница между `useMemo` и `useCallback`?](questions/day-037.md) |
| День 038 | `ASP.NET Core / Security` | [Как устроена JWT (JSON Web Token) аутентификация?](questions/day-038.md) |
| День 039 | `EF Core` | [Что такое проблема N+1 запросов в EF Core и как её избежать?](questions/day-039.md) |
| День 040 | `React / State` | [В чем разница между Redux Toolkit, TanStack Query (React Query) и Zustand?](questions/day-040.md) |

---

*Автоматически обновляется через GitHub Actions каждый день в 06:00 UTC.*
