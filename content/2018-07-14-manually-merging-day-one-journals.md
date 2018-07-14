title: Manually Merging Day One Journals
status: published
tags: python
slug: manually-merging-day-one-journals


My first Day One entry is from January 24, 2012. I used it often to take
note about what I was doing during my PhD with the `#wwid` tag (what was I
doing, an idea from [Brett Terpstra](http://brettterpstra.com/), I think), and
sometimes to clarify some thoughts.

When Day One went The Way of the Subscription, I didn't bother too much
because Dropbox sync still worked. Until it didn't. I somehow didn't realized
it and kept adding entries to both the iOS _and_ the macOS versions. Not
good. It's been on my to do list for a while to find a way to merge the two
journals. I could probably subscribe to the Day One sync service and have it
figure out the merging but I didn't want to subscribe just for that.

I learned somewhere that Day One 2 could export journals as a folder of photos
and a JSON file. I figure I could probably write a script to do the merging.
So I downloaded Day One 2 on my iPhone and Mac, imported my Day One Classic
journals, exported them as JSON to a folder on my Mac, and unzipped them. I
also created a `merged/` folder where to put the merged journal. The hierarchy
looks like this:

```sh
$ tree -L 2
.
├── Journal-JSON-ios/
│   ├── Journal.json
│   └── photos/
├── Journal-JSON-ios.zip
├── Journal-JSON-mac/
│   ├── Journal.json
│   └── photos/
├── Journal-JSON-mac.zip
├── merge_journals.py
└── merged/
```

I first copied the photo folder from `Journal-JSON-ios/` to `merged/`
and the photos from `Journal-JSON-mac/photos/`. I was pretty confident
that I would end up with the union of all the photos because Day One uses
[UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) to
identify each photo. The `-n` option to `cp` prevents overwriting files.

```sh
$ cp -r Journal-JSON-ios/photos merged/
$ cp -n Journal-JSON-mac/photos merged/photos/
```

I then ran the `merge_journals.py` script (below) to do a similar merge of the
entries, based on the UUIDs. The merging happens by building a dictionary with
UUID of each entry as the key and the entry itself as the value. It's two
loops over the iOS and the macOS entries. Entries with the same UUID should
have the same contents, unless I've edited some metadata on one platform but
not the other. I'm not too worried about that.

The output dictionary will be written to the `Journal.json` file. The entries
are sorted chronologically because that's how it was in the exported journal
files, but I doubt it matters.

The `output` dictionary is written to disk without enforcing the conversion to
ASCII since the exported journals are encoded using UTF-8. The indent is there
to make the output more readable and diff-able with the exported journals.


```python
import json

with open('./Journal-JSON-ios/Journal.json') as f:
    ios = json.load(f)
with open('./Journal-JSON-mac/Journal.json') as f:
    mac = json.load(f)

# Extract and merge UUIDs
uniques = {entry['uuid']: entry for entry in ios['entries']}
for entry in mac['entries']:
    uniques[entry['uuid']] = entry

# Create the output JSON data structure
output = {}
output['metadata'] = mac['metadata']
output['entries'] = list(uniques.values())
# I'm not sure it matters, but Day One usually exports the entries
# in chronological order
output['entries'].sort(key=lambda e: e['creationDate'])

# ensure_ascii print unicode characters as-is.
with open('merged/Journal.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=True, ensure_ascii=False)
```

The last step is to zip the journal and photos together, which tripped me up
a few times. The `Journal.json` and the `photos/` folder must be at the top
level of the archive, so I zip the file from within the `merged/` folder and
then move it back up one level.

```sh
$ cd merged
$ zip -r merged.zip *
$ mv merged.zip ..
```

I could then import `merged.zip` in Day One, which created a new Journal, and
delete the old one.


I guess I could somewhat automate this to roll my own, DIY, sync between
versions of Day One, but I'd rather pay them money once I decide to use Day
One frequently again. Still, I really appreciate that the Day One developers
picked formats that could be manipulated so easily.
