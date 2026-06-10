/**
 * Optional hook for the Fashion OS page.
 * Add this script after fashion-os-catalog.js and adapt selectors if your HTML uses different ids.
 */
(async function () {
  const form = document.querySelector('#fashion-os-form, form[data-fashion-os]');
  const input = document.querySelector('#fashion-prompt, textarea[name="prompt"], input[name="prompt"]');
  const refsContainer = document.querySelector('#fashion-os-references');
  const enrichedPromptField = document.querySelector('#fashion-enriched-prompt');

  if (!form || !input || !window.FashionOSCatalog) return;

  form.addEventListener('submit', async function (event) {
    const userPrompt = input.value || '';
    const references = await window.FashionOSCatalog.searchFashionCatalog(userPrompt, { limit: 8 });
    const enrichedPrompt = window.FashionOSCatalog.buildEnrichedFashionPrompt(userPrompt, references);

    if (refsContainer) window.FashionOSCatalog.renderFashionResults(refsContainer, references);
    if (enrichedPromptField) enrichedPromptField.value = enrichedPrompt;

    // Para integração com outro gerador de imagem, use:
    // window.dispatchEvent(new CustomEvent('fashion-os:prompt-enriched', { detail: { userPrompt, enrichedPrompt, references } }));
    window.dispatchEvent(new CustomEvent('fashion-os:prompt-enriched', {
      detail: { userPrompt, enrichedPrompt, references }
    }));
  });
})();
