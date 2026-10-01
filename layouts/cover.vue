<template>
  <div class="slidev-layout plain plain-cover" :class="{ 'plain-cover-english': $frontmatter.englishTitle }">
    <div v-if="$frontmatter.date" class="plain-date">{{ $frontmatter.date }}</div>
    <div class="plain-cover-title">
      <h1><slot /></h1>
      <p v-if="$frontmatter.subtitle" class="plain-subtitle">{{ $frontmatter.subtitle }}</p>
    </div>
    <div class="plain-cover-meta">
      <p v-if="$frontmatter.affiliation">{{ $frontmatter.affiliation }}</p>
      <p v-if="$frontmatter.group">{{ $frontmatter.group }}</p>
      <p class="plain-author">{{ $frontmatter.presenter || '' }}</p>
    </div>
  </div>
</template>
