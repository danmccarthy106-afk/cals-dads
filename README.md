# Cal's Dads

Events and RSVPs for the dads of Cal's Angels. Tom posts get-togethers, dads tap **I'm in / Maybe / Can't make it**, and Tom sees a live headcount with everyone's contact info.

- **Events**: upcoming events with date, time, place (map link), details, optional RSVP-by date, and optional "family & guests welcome" with a guest count. Every dad sees who's going, can leave a note for Tom, and can add the event to their calendar.
- **The dads**: a directory of each family: the dad's name, and each child's name, diagnosis, status (*in treatment*, *in remission*, *earned wings*) and a photo from treatment and one from remission. Phone and email appear only if the dad chooses to share them.
- **My family**: each dad keeps their family's info up to date.
- **WhatsApp**: every event has a *Share to WhatsApp* button for posting it in the group chat.
- **Organizer** (Tom only): paste in the WhatsApp group roster (names and numbers) so everyone counts in "No reply" even before joining the site, record RSVPs for dads who answer in the chat, and nudge anyone who hasn't replied with a one-tap WhatsApp message. Also: approve new dads; for each event, see going / maybe / can't / no reply with phone and email, email the dads who haven't replied, copy their numbers to text them, set an RSVP for a dad who called in, and download the list. Also download the whole directory.

Everything is private. Dads sign in with Google or email and password, and Tom approves each new dad before they can see events or other families.

Try it with sample data (kept only in your browser): open the site with `?demo` on the end of the address.

## Files

- `index.html` is the whole site: static, hosted on GitHub Pages, with data in Firebase (Firestore + Authentication).
- `img/` holds the Cal's Dads banner (a phone-sized copy is used on small screens).
- `firestore.rules` decides who can read and change what. **The organizer email list lives here.**

## One-time setup

Uses Firebase project `essence-trip-planner-2026` (the old trip planner's project; its data is no longer reachable).

1. **Turn on sign-in:** Firebase console → Authentication → Get started → Sign-in method → enable **Google** and **Email/Password**.
2. **Allow the site's address:** Authentication → Settings → Authorized domains → add `danmccarthy106-afk.github.io` (plus any custom domain).
3. **Set the organizers:** in `firestore.rules`, add Tom's email to `organizerEmails()` (Dan is already listed; add anyone else who should manage events). If Tom uses email/password rather than Google, he'll verify his email from the My family page first.
4. **Deploy the rules:** `firebase deploy --only firestore:rules`
5. Tom signs in, fills in his family, pastes the WhatsApp roster into the Organizer page (never commit it; this repo is public), and then shares the site link with the dads.

Photos are shrunk in the browser and stored in Firestore, so the free Spark plan is enough.
