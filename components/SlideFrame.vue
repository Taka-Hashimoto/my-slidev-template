<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'
const { $frontmatter, $slidev, $page } = useSlideContext()
const page = computed(() => $frontmatter.page ?? ($page.value - 1))
const numbered = computed(() => $frontmatter.numbered ?? $slidev.themeConfigs.pageNumbers ?? true)
</script>

<template>
  <div class="slidev-layout plain" :class="$frontmatter.bodyClass">
    <span v-if="numbered" class="plain-page">{{ page }}</span>
    <header class="plain-header">
      <p v-if="$frontmatter.section" class="plain-section">{{ $frontmatter.section }}</p>
      <h1 :class="{ 'plain-title-small': $frontmatter.smallTitle }">{{ $frontmatter.title }}</h1>
      <p v-if="$frontmatter.lead" class="plain-lead">{{ $frontmatter.lead }}</p>
    </header>
    <main class="plain-body"><slot /></main>
    <footer v-if="$slots.takeaway" class="plain-takeaway"><slot name="takeaway" /></footer>
    <div v-if="$slots.note" class="plain-note"><slot name="note" /></div>
  </div>
</template>
