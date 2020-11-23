# T81948 : Cursor disappearing in sculpt mode  in 2.91.0

Tags: bug

![T81948%20Cursor%20disappearing%20in%20sculpt%20mode%20in%202%2091%20%205b94ec367f4940668cc672987a0d5bf5/blenderfirstproblem.gif](T81948%20Cursor%20disappearing%20in%20sculpt%20mode%20in%202%2091%20%205b94ec367f4940668cc672987a0d5bf5/blenderfirstproblem.gif)

2.91.0

> that looks like conflict, cause there is a change in Blender (idk the commit) that **use brush cursor for every tool in SculptMode** so is only to check that patch and/or **poke to Pablo Dobarro** to check it out (maybe can filter annotation tool to let use tool icon instead of brush)

maybe something wrong at paint_poll? looks like there should filter if tool is a brush or not, but maybe is on a higher level
Ops, Edit: as with commit that also use brush cursor for non-brushes tools, should be a way to filter if that non-brush tool is annotate or not

The relevant commit is this 

```bash
commit b9e469664188ac675f3743e8d3938f34c996957e
Author: Pablo Dobarro <pablodp606@gmail.com>
Date:   Thu Oct 1 01:52:40 2020 +0200

    Sculpt: Show paint brush cursor in all tools
    
    This patch enables the paint brush cursor with all tools in sculpt mode,
    even with the ones that are not brushes. The motivations for this change
    are:
    - The filters are using the position of the active vertex for certain
    features without any visualization of what the active vertex is.
    
    - You can call operators like mask expand (which depends on the brush
    cursor position and active vertex) with a non brush tool enabled.
    
    - Having the cursor in the rest of the tools allows to have a scene
    scale representation of the radius and a direct control of radius and
    strength (using the current brush shortcuts), which will allow to make
    features more intuitive without relying on modifying values in the
    topbar. For example, the brush radius can be used to control the depth
    of the cut in the trimming tools or the size of the sphere in the
    sphere mesh filter
    
    Reviewed By: #user_interface, dbystedt, pablovazquez
    
    Differential Revision: https://developer.blender.org/D9071
```