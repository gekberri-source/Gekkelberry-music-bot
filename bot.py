Gekkelberry Music Bot — Recommendation Upgrade

Goal

Improve the existing Telegram music bot so that it behaves like a serious music-discovery tool rather than a generic “similar artists” bot.

Do NOT redesign the existing Telegram token/environment setup. The bot must continue reading TELEGRAM_BOT_TOKEN from the environment/Codespaces Secret. Never print, expose, log, or ask for the token.

1. Input

When the user sends an artist name or track name, identify what they most likely mean.

The input may be:

• an artist name;
• a track title;
• an artist + track;
• Russian or international music.

2. Genre/style identification

Determine the most musically useful genre/subgenre, not a broad marketing category.

Use multiple relevant descriptors when appropriate, for example:

• microhouse
• minimal house
• minimal techno
• tech house
• breakbeat
• electro
• jungle
• IDM
• experimental electronic
• alternative rock
• post-punk

Avoid vague labels such as “electro dance” when a more precise style is available.

Example:
Ricardo Villalobos should normally be classified around:
microhouse / minimal techno / minimal house / techno

Do not force every artist into a single genre.

3. Recommendation quality

Return 5 REAL track recommendations.

Recommendations must be based on actual musical similarity, considering as many of these as can be reliably determined:

• genre/subgenre;
• rhythm and drum pattern;
• groove;
• BPM/tempo range;
• instrumentation;
• production style;
• scene/label context;
• era;
• overall sonic character.

Do NOT recommend an artist merely because they are broadly popular with listeners of the input artist.

For Russian artists, do NOT default to mainstream Russian rock/pop simply because the artist is Russian.

The goal is musical similarity, not demographic similarity.

4. Real tracks only

Every recommendation must be a real artist + real track.

NEVER invent:

• artists;
• track titles;
• labels;
• URLs.

If a recommendation cannot be verified, omit it.

5. Listening links

Do NOT use Deezer or Spotify.

Prefer sources in this order:

1. Bandcamp
2. SoundCloud
3. YouTube / YouTube Music
4. Another genuinely accessible music source only if necessary

Only provide a URL when it points to the exact artist/track being recommended.

Do not generate a guessed search URL and present it as the track page.

If an exact listening page cannot be reliably found, omit the link rather than inventing one.

6. Telegram response format

Keep the response compact and easy to read in Telegram.

Use approximately this structure:

Artist — Track

Style: microhouse / minimal techno

Similar tracks:

1. Artist — Track
Why: short, specific reason
Source: Bandcamp — real URL
2. Artist — Track
Why: short, specific reason
Source: SoundCloud — real URL

Continue to 5 recommendations when 5 verified recommendations are available.

Do not write long essays.

7. Source verification

Before returning a link, verify that:

• the artist exists;
• the track exists;
• the URL corresponds to that exact track;
• the source is not Deezer or Spotify.

If the available information is uncertain, do not fabricate confidence.

8. Test cases

After implementing the changes, test the bot with:

Test A

Input:
АукцЫон

The recommendations should be genuinely musically related to АукцЫон. Avoid random mainstream Russian recommendations unless there is a clear musical reason.

Test B

Input:
Ricardo Villalobos

The style classification should be close to:
microhouse / minimal techno / minimal house / techno

It should NOT classify Ricardo Villalobos simply as “electro dance”.

Recommendations should be specific tracks, not only artist names.

9. Important implementation constraint

Preserve all existing working Telegram functionality.

Do not remove the current token/environment configuration.

Do not expose or print TELEGRAM_BOT_TOKEN.

Do not put the token into source code, configuration files, task files, logs, HTTP debug output, or error messages.

10. Final verification

After modifying the project:

1. Run/test the bot.
2. Confirm that the Telegram bot starts successfully.
3. Test both АукцЫон and Ricardo Villalobos.
4. Confirm that recommendations are tracks, not only artists.
5. Confirm that returned URLs are real and correspond to the exact tracks.
6. Confirm that no Deezer or Spotify links are returned.
7. Confirm that the Telegram token is not printed in logs.

If something cannot be reliably verified, prefer omitting it over inventing it.

Do not ask the user for the Telegram token.
