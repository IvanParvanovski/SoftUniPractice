import { Directive, ElementRef, Input, OnDestroy, OnInit, Renderer2, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appMyRouterLink]'
})
export class MyRouterLinkDirective  implements OnDestroy, OnInit{
  @Input() appMyRouterLink!: string;
  @Input() template!: TemplateRef<any>;

  unsub: (() => void) | null = null;

  viewHasBeenCreated = false;

  constructor(
    private elementRef: ElementRef,
    private renderer: Renderer2,
    private vc: ViewContainerRef
  ) { 
    // console.log(elementRef);
    
    this.unsub = this.renderer.listen(this.elementRef.nativeElement, 'mouseover', this.mouseOverHandler);
    this.unsub = this.renderer.listen(this.elementRef.nativeElement, 'mouseleave', this.mouseLeaveHandler);

    // this.renderer.setAttribute(this.elementRef.nativeElement, 'data-test', '123');
  }

  mouseOverHandler = (e: MouseEvent) => {
    if (this.viewHasBeenCreated) {return;}

    this.renderer.setStyle(this.elementRef.nativeElement, 'color', 'red');    
    this.vc.createEmbeddedView(this.template);
    this.viewHasBeenCreated = true;
  }

  mouseLeaveHandler = (e: MouseEvent) => {
    this.renderer.setStyle(this.elementRef.nativeElement, 'color', 'initial');
    
    this.vc.clear();
    this.viewHasBeenCreated = false;
  }

  ngOnInit(): void {
    console.log(this.appMyRouterLink);
    console.log(this.template);
    
    this.vc.createEmbeddedView(this.template);
  }

  ngOnDestroy(): void {
    // this.unsubs.forEach(fn => fn());
    this.unsub?.call(undefined);
  }
}
