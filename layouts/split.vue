<template>
  <SlideFrame>
    <div class="plain-cols" :style="{ gridTemplateColumns: $frontmatter.ratio || '1fr 1fr' }">
      <section class="plain-column"><slot /></section>
      <section class="plain-column"><slot name="right" /></section>
    </div>
    <template v-if="$slots.takeaway" #takeaway><slot name="takeaway" /></template>
    <template v-if="$slots.note" #note><slot name="note" /></template>
  </SlideFrame>
</template>
