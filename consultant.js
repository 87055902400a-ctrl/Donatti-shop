/**
 * DONATTI AI — Движок трихологического консультанта
 * Зависимости: translations.js, hair_problems_database.js
 *
 * Состояния:
 *   idle       — начальное, ждём описания проблемы
 *   clarifying — задаём уточняющие вопросы (до 2 штук)
 *   open       — диагноз поставлен, можно задать следующий вопрос
 */

class ConsultantEngine {
  constructor() {
    this.reset();
  }

  reset() {
    this.stage             = 'idle';
    this.detectedKey       = null;
    this.questionIndex     = 0;
    this.collectedAnswers  = [];
  }

  /** Возвращает поле объекта с учётом текущего языка */
  _lf(obj, field) {
    const uzField = field + '_uz';
    if (window.LANG === 'uz' && obj[uzField]) return obj[uzField];
    return obj[field];
  }

  /**
   * Главный вход: принимает текст → возвращает {message, buttons}
   * buttons: [{label, section}] — для перехода в каталог
   */
  handleInput(text) {
    const txt = text.trim();
    if (!txt) return null;

    if (this.stage === 'clarifying') {
      return this._onClarifyingAnswer(txt);
    }

    // idle или open → анализируем симптомы заново
    return this._analyzeAndAsk(txt);
  }

  // ── Анализ входящего сообщения ──────────────────────────────────
  _analyzeAndAsk(text) {
    const results = analyzeSymptoms(text);

    if (results.length === 0) {
      this.stage = 'idle';
      return {
        message: t('cons_unclear'),
        buttons: null
      };
    }

    const top = results[0];
    this.detectedKey      = top.key;
    this.questionIndex    = 0;
    this.collectedAnswers = [];
    this.stage            = 'clarifying';

    const cond = top.condition;
    const questions = this._lf(cond, 'clarifyingQuestions');
    const q = questions[0];

    return {
      message:
        this._lf(cond, 'empathy') + '\n\n' +
        t('cons_clarify_prefix') + '\n\n' +
        `❓ ${q}`,
      buttons: null
    };
  }

  // ── Обработка ответа на уточняющий вопрос ────────────────────────
  _onClarifyingAnswer(text) {
    const cond      = SCALP_CONDITIONS[this.detectedKey];
    const questions = this._lf(cond, 'clarifyingQuestions');

    this.collectedAnswers.push({ q: questions[this.questionIndex], a: text });
    this.questionIndex++;

    // Задаём второй вопрос (если есть и это ещё первый ответ)
    if (this.questionIndex === 1 && questions.length > 1) {
      return {
        message: `❓ ${questions[1]}`,
        buttons: null
      };
    }

    // Достаточно — формируем диагноз
    return this._generateDiagnosis();
  }

  // ── Итоговое сообщение с диагнозом ──────────────────────────────
  _generateDiagnosis() {
    const cond = SCALP_CONDITIONS[this.detectedKey];
    this.stage = 'open';

    const primary   = cond.products.find(p => p.role === 'primary');
    const secondary = cond.products.find(p => p.role === 'secondary');

    let msg = '';

    msg += `${t('cons_diagnosis_label')} ${this._lf(cond, 'problemDescription')}\n\n`;
    msg += `${t('cons_causes_label')} ${this._lf(cond, 'causes')}\n\n`;
    msg += `${t('cons_helps_label')}\n`;

    if (primary) {
      msg += `\n✅ **${primary.section}** — ${t('cons_primary_label')}\n`;
      msg += `${this._lf(primary, 'reason')}\n`;
    }
    if (secondary) {
      msg += `\n➕ **${secondary.section}** — ${t('cons_secondary_label')}\n`;
      msg += `${this._lf(secondary, 'reason')}\n`;
    }

    msg += `\n${this._lf(cond, 'disclaimer')}`;
    msg += `\n\n${t('cons_catalog_invite')}`;

    const buttons = cond.products.map(p => ({
      label:   `🛍 ${p.section}`,
      section: p.section
    }));

    return { message: msg, buttons };
  }
}

// Единственный экземпляр движка
const consultantEngine = new ConsultantEngine();
