---
name: Ignition
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434655'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#943700'
  on-tertiary: '#ffffff'
  tertiary-container: '#bc4800'
  on-tertiary-container: '#ffede6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#7d2d00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-table:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  container-padding: 24px
  gutter: 16px
  sidebar-width: 260px
  topbar-height: 64px
---

## Brand & Style
The design system is engineered for high-performance workforce management, balancing the energy of a startup with the reliability of enterprise software. The brand personality is efficient, decisive, and empowering.

The aesthetic follows a **Corporate / Modern** style with heavy influences from **Minimalism**. It prioritizes data density and legibility without feeling cluttered. The visual language uses ample white space to reduce cognitive load during complex administrative tasks, while utilizing high-contrast accents to draw attention to critical actions and system statuses.

## Colors
The palette is anchored by a "Spark Blue" primary, representing the energy of the brand name. 

- **Primary (Spark Blue):** Used for primary actions, active navigation states, and progress indicators.
- **Secondary (Slate):** Used for secondary text, icons, and non-critical UI elements to maintain a professional hierarchy.
- **Semantic Colors:** 
    - **Success (Emerald):** Reserved strictly for 'Active' employee statuses and completed workflows.
    - **Warning (Amber):** Used for 'On Leave', 'Pending' approvals, or time-sensitive alerts.
- **Neutrals:** A range of cool grays provides the structural scaffolding, using #F8FAFC for background surfaces to keep the interface feeling airy and modern.

## Typography
This design system utilizes **Inter** for its exceptional legibility in data-heavy environments. The typographic scale is optimized for information density.

- **Headlines:** Use tighter letter spacing and heavier weights to create a strong visual anchor for page titles.
- **Body:** The default size is 14px (body-md) to allow for more content visibility in tables and lists.
- **Labels:** Uppercase styles with slight letter spacing are used for table headers and section overviews to differentiate meta-data from primary content.
- **Data Tables:** A specific 13px size is utilized for row data to maximize the number of visible records while maintaining high readability.

## Layout & Spacing
The layout follows a **Fixed Sidebar / Fluid Content** model. 

- **Grid:** A 12-column grid is used for dashboard layouts, while data tables occupy the full width of the primary content container.
- **Desktop:** The sidebar is fixed at 260px. Content margins are set to 24px to provide a professional "breathing room" around data tables.
- **Tablet:** The sidebar collapses into an icon-only rail (72px) to prioritize workspace.
- **Mobile:** The sidebar becomes a hidden drawer, and container padding reduces to 16px. Vertical rhythm is maintained using a 4px baseline shift.

## Elevation & Depth
This design system employs **Tonal Layers** for its primary structure and **Ambient Shadows** for temporary overlays.

- **Level 0 (Background):** #F8FAFC. The base canvas for the entire application.
- **Level 1 (Cards/Tables):** Pure white (#FFFFFF) with a 1px border (#E2E8F0). No shadows are used for standard containers to maintain a clean, flat aesthetic.
- **Level 2 (Modals/Slide-overs):** White surfaces with an extra-diffused, low-opacity shadow (0px 10px 25px rgba(0,0,0,0.05)). This provides clear separation without the heaviness of traditional skeuomorphism.
- **Interactions:** Subtle 1px inner shadows may be used on pressed button states to indicate physical displacement.

## Shapes
The shape language is **Soft** and professional. 

- **Components:** Standard buttons, input fields, and cards use a 4px (0.25rem) corner radius. This provides a modern touch while maintaining the serious, structured feel of a management tool.
- **Badges:** Status badges use a higher `rounded-xl` (12px) radius to create a distinct visual pill shape that separates status indicators from clickable buttons.
- **Avatars:** Employee profile photos should always be rendered as perfect circles to contrast against the otherwise rectilinear grid.

## Components
Consistent component implementation is vital for user efficiency.

- **Data Tables:** Use a flat style with 1px horizontal dividers only (#F1F5F9). Row hover states should use a subtle tint of the primary color at 2% opacity.
- **Buttons:** 
    - *Primary:* Solid Spark Blue with white text.
    - *Ghost:* No background or border; Spark Blue text. Use for secondary actions like 'Cancel' or 'View Details'.
- **Status Badges:** 
    - *Active:* Light Green background (10% opacity) with dark Green text.
    - *On Leave:* Light Amber background (10% opacity) with dark Amber text.
- **Sidebars:** Use a dark theme (Slate 900) or a very light theme (White) depending on the brand implementation; for Ignition, a clean White sidebar with a 1px right-border is preferred.
- **Input Fields:** Use a 1px border (#D1D5DB). On focus, the border shifts to Spark Blue with a 3px soft outer glow in the same color at 10% opacity.
- **Slide-overs:** Always emerge from the right side of the screen, covering 400px - 600px of width, utilizing the Level 2 shadow defined in Elevation.