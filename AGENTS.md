# ArtBalkon-v2 Workflow Rules

## mandatory: Local verification before push

**Never push to GitHub without first verifying the site locally.**

### Required local check sequence:

1. **Start local server** (if needed):
   ```powershell
   npx serve
   ```
   or open `index.html` directly in browser.

2. **Verify visual correctness:**
   - Hero section scaling
   - Mobile responsiveness (no blank/flicker screens)
   - Quiz pricing displays correctly
   - All tabs/accordions functional

3. **Run JS syntax check** (automated):
   ```powershell
   node .\opencode\test_scripts_vm.mjs
   ```
   Must output: `Script #1: SYNTAX OK`, `Script #2: SYNTAX OK`, `Script #3: SYNTAX OK`

4. **Run quiz verification** (automated):
   ```powershell
   python .\opencode\quiz_verify.py
   ```
   Must output: `saved` at the end.

5. **Check GitHub Pages link:**
   - https://wadim0041.github.io/artbalcon/
   - Open in new incognito window
   - Verify no JS errors in console

### Push workflow:

```
❌ DO NOT push until all 5 checks pass ✅

After local verification passes:
1. git add index.html (and only index.html)
2. git commit -m "descriptive message"
3. git push origin main
4. Wait 1-2 minutes for GitHub Pages update
5. Re-verify live link with Ctrl+F5
```

### Exception cases:
- Emergency hotfixes require team lead approval
- Documentation-only changes may skip JS syntax check with justification

## standing rule: Визуал + скорость загрузки

**Нам нужен живой необыкновенный визуал (анимации, эффекты, живой бэкграунд), но скорость прогрузки и загрузки сайта — всегда в приоритете. Каждое визуальное изменение проектируй сразу в паре с перфомансом.**

### Требования к визуальным правкам:
- Только GPU-дешёвые свойства для анимаций (`transform`, `opacity`); никаких новых бесконечных циклов без стопа в простое (как rAF-стоп в витрине идей).
- Никаких новых внешних запросов/библиотек без необходимости; картинки — локально, сжатые, `loading="lazy"`, `decoding="async"`.
- Не двигать React-узлы через DOM (краш reconciler'а) — переупорядочивание только через CSS `order`; бандл не правим.
- Любая правка неба/фона: те же rAF и слои, только числа кривых; контраст текста проверять скриншотами (десктоп + мобилка).
- В отчёт каждого изменения: дельта веса (байты), число новых скриптов/анимаций, скриншот до/после.