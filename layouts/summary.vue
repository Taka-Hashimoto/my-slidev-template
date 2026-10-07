<template>
  <SlideFrame>
    <div v-if="$slots.figure" class="plain-cols">
      <section class="plain-column"><slot name="figure" /></section>
      <section class="plain-column"><div class="plain-summary"><slot /></div></section>
    </div>
    <div v-else class="plain-summary"><slot /></div>
    <template v-if="$slots.takeaway" #takeaway><slot name="takeaway" /></template>
    <template v-if="$slots.note" #note><slot name="note" /></template>
  </SlideFrame>
</template>
