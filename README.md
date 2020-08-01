<p>
    <a href="https://yoriiis.github.io/storelocatorjs" title="storelocatorjs">
        <h2 align=center>Storelocatorjs <small>static with Google Maps</small></h2>
    </a>
</p><br />

<p align="center">
    <strong>This is fork of original storelocatorjs.</strong>
    Visit <a href="https://yoriiis.github.io/storelocatorjs" title="yoriiis.github.io/storelocatorjs">yoriiis.github.io/storelocatorjs</a> for original version of storelocatorjs.
    The difference is that data is obtained through resource added to your website.</strong>
</p>

---

## Usage

Main difference between this version and original Storelocatorjs is that you don't use the cloud function. You must add
map object to the scope which will contain stores/POI's grouped by their category. See ```small-data.js``` from examples.
Be aware that large number of markers can affect the performance. Example with clusters uses more than 1k markers from
 ```data.js``` to show that it can be slow. Other diffrences:
 * no distance calculation
 * added dev build to npm
 * no limit on stores

Rest is the same as in the original Storelocatorjs project.
