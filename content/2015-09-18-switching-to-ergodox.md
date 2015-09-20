Title: Switching to ErgoDox
Status: draft

I've had pet peeves with standard layout keyboards for as long as I can remember. The slanted and unbalanced layout have always seemed so illogical to me. I'm well aware of why but when so many other things have been changed on computers they have remained essentially untouched (at least in layout).

My first attempt at doing something about this was an [ErgoDox](http://deskthority.net/wiki/ErgoDox), which is a matrix layout, fully firmware programmable, split keyboard. Building it involved buying all the parts from Massdrop, learning to solder, "borrowing" the kitchen table for a weekend, and a couple of singed fingers.This was the first time I've really done a hardware project and it was fascinating to dive into that world.

![ErgoDox Buildstation](/images/ergodox-buildstation.jpg)

I have the standard edition (as opposed to full hand with wrist wrests built into the case) with Cherry Brown switches and black, blank PBT DCS keycaps.

I adore it.

Initially I tried to learn Norman thinking I would treat it as an entirely separate input device and easily maintain my QWERTY typing speed. I lasted about 3 months with mixed results. My QWERTY suffered slightly (down ~10wpm with prose, more with typing), I got up to ~85wpm in Norman writing prose but programming in it was a nightmare. Luckily switching to QWERTY wasn't too hard, but did involve learning it on the ErgoDox. Please don't take this as a reason to not try Norman, it's a fantastic layout and was noticeably nicer to write prose with.

Configuring the layout of an ErgoDox feels very similar to tweaking an editor config so obviously I've <del>wasted</del>enjoyed many hours doing it. Massdrop provide a really useful [online editor](https://www.massdrop.com/ext/ergodox/) which is a great place to start. When you need more functionality the [tmk keyboard](https://github.com/cub-uanic/tmk_keyboard) project is great but requires editing C files.

The ErgoDox uses a layer system, essentially modifier keys on steroids. Layers are pushed and popped from a stack and each layer is a completely *separate* keyboard. Keys can be assigned to push, pop, and switch layers (switch layers appears to work by pushing on key down and popping on key up). My current firmware makes use of this by switching to media keys when the [inner wing keys are held down](https://github.com/ghickman/tmk_keyboard/blob/master/keyboard/ergodox/keymap_qwerty.h#L88). However a gaming layer may appear in the future so I only need the left-hand side in-game.

You can find my full QWERTY-based [on github](https://github.com/ghickman/tmk_keyboard/blob/master/keyboard/ergodox/keymap_qwerty.h).
