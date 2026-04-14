#!/usr/bin/env node

import { GoogleGenAI } from "@google/genai";
import { writeFileSync, mkdirSync } from "fs";
import { join, resolve } from "path";

// ─── Config ──────────────────────────────────────────────────────────────────

const SAIDA_DIR = resolve("../videos");

// ─── Args ────────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);

function getArg(flag, fallback) {
  const i = args.indexOf(flag);
  return i !== -1 && args[i + 1] ? args[i + 1] : fallback;
}

function showHelp() {
  console.log(`
Uso:
  node gerar-video.js --prompt "..." [opções]

Opções:
  --prompt      Texto descrevendo o vídeo (obrigatório)
  --proporcao   16:9 | 9:16              (padrão: 16:9)
  --duracao     5 | 6 | 8               (padrão: 8)
  --pessoas     allow_all | allow_adult | dont_allow  (padrão: allow_all)
  --nome        Nome do arquivo de saída sem extensão
  --help        Exibe esta ajuda

Exemplos:
  node gerar-video.js --prompt "Personagem verde de pé num quarto de luxo..." --proporcao 9:16
  node gerar-video.js --prompt "..." --duracao 8 --nome cena-quarto
`);
  process.exit(0);
}

if (args.includes("--help") || args.length === 0) showHelp();

const prompt    = getArg("--prompt",    null);
const proporcao = getArg("--proporcao", "16:9");
const duracao   = getArg("--duracao",   "8");
const pessoas   = getArg("--pessoas",   "allow_all");
const nomeArq   = getArg("--nome",      null);

if (!prompt) {
  console.error("Erro: --prompt é obrigatório.\n");
  showHelp();
}

// ─── Auth ─────────────────────────────────────────────────────────────────────

if (!process.env.GEMINI_API_KEY) {
  console.error("Erro: variável GEMINI_API_KEY não definida.");
  console.error("Obtenha sua chave em: aistudio.google.com/apikey");
  console.error("Execute: export GEMINI_API_KEY=sua_chave\n");
  process.exit(1);
}

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// ─── Geração ──────────────────────────────────────────────────────────────────

console.log("\n🎬 Veo 2 — Gerando vídeo...");
console.log(`   Proporção:  ${proporcao}`);
console.log(`   Duração:    ${duracao}s`);
console.log(`   Prompt: "${prompt.slice(0, 80)}${prompt.length > 80 ? "..." : ""}"\n`);

const inicio = Date.now();

let operation = await ai.models.generateVideos({
  model: "veo-2.0-generate-001",
  prompt,
  config: {
    aspectRatio:      proporcao,
    durationSeconds:  duracao,
    personGeneration: pessoas,
    numberOfVideos:   1,
  },
});

console.log("   Aguardando geração...");

while (!operation.done) {
  await new Promise(r => setTimeout(r, 10000));
  operation = await ai.operations.getVideosOperation({ operation });
  process.stdout.write(".");
}

console.log("\n");

// ─── Download ─────────────────────────────────────────────────────────────────

const video = operation.response.generatedVideos?.[0]?.video;

if (!video) {
  console.error("Erro: nenhum vídeo gerado.");
  console.error(JSON.stringify(operation, null, 2));
  process.exit(1);
}

const durMs       = ((Date.now() - inicio) / 1000).toFixed(1);
const data        = new Date().toISOString().slice(0, 16).replace(/[T:]/g, "-");
const nomeBase    = nomeArq ?? `veo2-${data}`;
const nomeArquivo = `${nomeBase}_${proporcao.replace(":", "x")}_${duracao}s.mp4`;

mkdirSync(SAIDA_DIR, { recursive: true });
const caminhoSaida = join(SAIDA_DIR, nomeArquivo);

await ai.files.download({ file: video, downloadPath: caminhoSaida });

console.log(`✅ Concluído em ${durMs}s`);
console.log(`   Arquivo: ${caminhoSaida}\n`);
