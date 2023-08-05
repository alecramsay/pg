// Take a screenshot of map in DRA, using headless Chrome.
//
// To build:
// tsc scripts/screenshot.ts
//
// To run:
// node scripts/screenshot.js
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var _this = this;
var puppeteer = require('puppeteer');
// TODO - add command line args:
// - map guid 
// - image path
// const [url, pathInput] = process.argv.slice(2);
// if (url === undefined) {
//   console.log("Usage: node mapscreenshot.js <url> [<screenshot PNG path>]");
// }
var url = 'https://davesredistricting.org/maps#viewmap::bbd90d8a-b4c3-4875-8ffe-4f931e141211';
// const url = 'https://www.nakedcapitalism.com/';
// const url = 'https://davesredistricting.org/';
var screenshotPath = "/Users/alecramsay/Downloads/screenshot.png";
// const screenshotPath = pathInput ?? "screenshot.png";
(function () { return __awaiter(_this, void 0, void 0, function () {
    var browser, page, canvas, e_1;
    return __generator(this, function (_a) {
        switch (_a.label) {
            case 0: return [4 /*yield*/, puppeteer.launch({ headless: "new" })];
            case 1:
                browser = _a.sent();
                _a.label = 2;
            case 2:
                _a.trys.push([2, 9, 10, 12]);
                return [4 /*yield*/, browser.newPage()];
            case 3:
                page = _a.sent();
                // await page.setViewport({width: 2560, height: 1600});
                // await page.setViewport({width: 1998, height: 1394});
                return [4 /*yield*/, page.setViewport({ width: 1280, height: 1024 })];
            case 4:
                // await page.setViewport({width: 2560, height: 1600});
                // await page.setViewport({width: 1998, height: 1394});
                _a.sent();
                console.log("Loading the page. This can take 30 seconds or so... ");
                return [4 /*yield*/, page.goto(url, { waitUntil: ['load', 'domcontentloaded', 'networkidle0'], timeout: 0 })];
            case 5:
                _a.sent();
                return [4 /*yield*/, page.addStyleTag({
                        content: '.MuiModal-backdrop, .MuiDialog-container, .MuiButtonBase-root, .MuiTypography-root, .mapboxgl-control-container { display: none; }'
                    })];
            case 6:
                _a.sent();
                return [4 /*yield*/, page.$('canvas')];
            case 7:
                canvas = _a.sent();
                console.log("Saving PNG to ".concat(screenshotPath, "..."));
                return [4 /*yield*/, canvas.screenshot({ type: 'png', path: screenshotPath })];
            case 8:
                _a.sent();
                console.log("Done!");
                return [3 /*break*/, 12];
            case 9:
                e_1 = _a.sent();
                console.log(e_1);
                return [3 /*break*/, 12];
            case 10: return [4 /*yield*/, browser.close()];
            case 11:
                _a.sent();
                return [7 /*endfinally*/];
            case 12: return [2 /*return*/];
        }
    });
}); })();
// Resources:
// - https://developer.chrome.com/blog/headless-chrome/
// - https://developer.chrome.com/docs/puppeteer/
// - https://pptr.dev/
