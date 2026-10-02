(() => {
    "use strict";

    const init = () => {
        document.documentElement.classList.add("js-ready");

        document.querySelectorAll("img:not([loading])").forEach((image) => {
            image.loading = "lazy";
            image.decoding = "async";
        });

        document.querySelectorAll("a[href]:not([data-navigation-bound])").forEach((link) => {
            link.dataset.navigationBound = "true";
            link.addEventListener("click", (event) => {
                if (
                    event.defaultPrevented ||
                    event.button !== 0 ||
                    event.metaKey ||
                    event.ctrlKey ||
                    event.shiftKey ||
                    event.altKey ||
                    link.target === "_blank"
                ) {
                    return;
                }

                if (link.origin === window.location.origin) {
                    event.preventDefault();
                    navigate(link.href);
                    return;
                }

                link.classList.add("is-loading");
            });
        });

        updateActiveMenu();
    };

    const updateActiveMenu = () => {
        const currentPath = window.location.pathname;

        document.querySelectorAll(".muc-menu").forEach((link) => {
            const linkPath = new URL(link.href, window.location.origin).pathname;
            link.classList.toggle("dang-chon", linkPath === currentPath);
        });
    };

    const updatePageStyles = (documentFragment) => {
        const pageStyleSelector = [
            'link[href*="/static/cssnhanvien/"]:not([href$="/style.css"])',
            'link[href*="/static/cssquanly/"]:not([href$="/style.css"])'
        ].join(", ");

        document.querySelectorAll(`${pageStyleSelector}, link[data-page-style]`)
            .forEach((link) => link.remove());

        documentFragment.querySelectorAll(pageStyleSelector).forEach((source) => {
            const link = document.createElement("link");
            link.rel = "stylesheet";
            link.href = source.href;
            link.dataset.pageStyle = "true";
            document.head.appendChild(link);
        });
    };

    const navigate = async (url, addToHistory = true) => {
        const content = document.querySelector(".noi-dung");
        if (!content || content.dataset.loading === "true") return;

        content.dataset.loading = "true";
        content.classList.add("is-loading");

        try {
            const response = await fetch(url, {
                headers: { "X-Requested-With": "fetch" }
            });

            if (!response.ok) throw new Error(`Navigation failed: ${response.status}`);

            const html = await response.text();
            const page = new DOMParser().parseFromString(html, "text/html");
            const nextContent = page.querySelector(".noi-dung");

            if (!nextContent) throw new Error("Page content was not found");

            content.replaceWith(nextContent);
            updatePageStyles(page);
            document.title = page.title;

            if (addToHistory) window.history.pushState({}, "", url);
            updateActiveMenu();
            init();
            window.scrollTo({ top: 0, behavior: "smooth" });
        } catch (error) {
            window.location.assign(url);
        } finally {
            const currentContent = document.querySelector(".noi-dung");
            if (currentContent) {
                currentContent.dataset.loading = "false";
                currentContent.classList.remove("is-loading");
            }
        }
    };

    document.addEventListener("visibilitychange", () => {
        document.documentElement.classList.toggle(
            "page-hidden",
            document.visibilityState === "hidden"
        );
    });

    window.addEventListener("popstate", () => navigate(window.location.href, false));

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init, { once: true });
    } else {
        init();
    }
})();
